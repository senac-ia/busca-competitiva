from jogo import Jogo, JogadorHumano, JogadorAgente, Jogada

class JogadaVelha(Jogada):
  def __init__(self, posicao_quadrante):
    self.posicao_quadrante = posicao_quadrante

  def e_valida(self, jogo):
    return self.posicao_quadrante >= 0 and self.posicao_quadrante <= 8 and\
      jogo.posicao[self.posicao_quadrante] == "⬜"

class JogadorVelhaHumano(JogadorHumano):
  def jogar(self, jogo):
    jogada = JogadaVelha(-1)
    while not jogada.e_valida(jogo):
      posicao_quadrante = int(input("Escolha um quadrado (1-9): "))
      jogada.posicao_quadrante = posicao_quadrante - 1 # 1-9 -> 0-8
    return jogada

class JogoVelha(Jogo):
  def __init__(self, estado = ["⬜"] * 9, jogador_turno = None):
    self.posicao = estado
    self.jogador_turno = jogador_turno

  def inicializar_jogadores(self):
    (humano, agente) = (JogadorVelhaHumano("❌"), JogadorAgente("🔵"))
    humano.define_proximo_turno(agente)
    agente.define_proximo_turno(humano)

    self.jogador_turno = humano

    return (humano, agente)

  def turno(self):
    return self.jogador_turno
  
  def jogar(self, jogada):
    novo_estado = self.posicao.copy()
    novo_estado[jogada.posicao_quadrante] = self.jogador_turno.imprimir()
    return JogoVelha(novo_estado, self.jogador_turno.proximo_turno())

  def gerar_jogos_validos(self):
    return [JogadaVelha(quadrante) for quadrante in range(len(self.posicao)) if self.posicao[quadrante] == "⬜"]
  
  def venceu(self):
    return self._venceu_linhas(self.posicao) or \
    self._venceu_colunas(self.posicao) or \
    self._venceu_diagonal(self.posicao)
  
  def imprimir_jogada(self, jogador, jogada):
    return f"{jogador.imprimir()} jogou {jogada.posicao_quadrante + 1} ({self.posicao[jogada.posicao_quadrante]})"
  
  def imprimir(self):
    return f"""{self.posicao[0]}|{self.posicao[1]}|{self.posicao[2]}
---------
{self.posicao[3]}|{self.posicao[4]}|{self.posicao[5]}
---------
{self.posicao[6]}|{self.posicao[7]}|{self.posicao[8]}"""

  def calcular_utilidade(self, jogador):
    if self.venceu() and self.jogador_turno == jogador:
      return -1
    elif self.venceu() and self.jogador_turno != jogador:
      return 1
    else:
      return 0
    
  #######################################
  #### Funções auxiliares - privadas ####
  #######################################

  # linhas iguais e não é "⬜"
  def _venceu_linhas(self, posicao):
    return posicao[0] == posicao[1] and posicao[0] == posicao[2] and posicao[0] != "⬜" or \
      posicao[3] == posicao[4] and posicao[3] == posicao[5] and posicao[3] != "⬜" or \
      posicao[6] == posicao[7] and posicao[6] == posicao[8] and posicao[6] != "⬜"

  # colunas iguais e não é "⬜"
  def _venceu_colunas(self, posicao):
    return posicao[0] == posicao[3] and posicao[0] == posicao[6] and posicao[0] != "⬜" or \
      posicao[1] == posicao[4] and posicao[1] == posicao[7] and posicao[1] != "⬜" or \
      posicao[2] == posicao[5] and posicao[2] == posicao[8] and posicao[2] != "⬜"

  # diagonal iguais e não é "⬜"
  def _venceu_diagonal(self, posicao):
    return posicao[0] == posicao[4] and posicao[0] == posicao[8] and posicao[0] != "⬜" or \
      posicao[2] == posicao[4] and posicao[2] == posicao[6] and posicao[2] != "⬜"
