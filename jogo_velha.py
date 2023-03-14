from jogo import Jogo, JogadorHumano, JogadorAgente, Jogada

class JogadaVelha(Jogada):
  def __init__(self, posicao_quadrante):
    self.posicao_quadrante = posicao_quadrante

  def e_valida(self, jogo):
    return self.posicao_quadrante >= 0 and self.posicao_quadrante <= 8 and\
      jogo.estado[self.posicao_quadrante] == "⬜"

class JogadorVelhaHumano(JogadorHumano):
  def jogar(self, jogo):
    jogada = JogadaVelha(-1)
    while not jogada.e_valida(jogo):
      posicao_quadrante = int(input("Escolha um quadrado (1-9): "))
      jogada.posicao_quadrante = posicao_quadrante - 1 # 1-9 -> 0-8
    return jogada

class JogoVelha(Jogo):
  def __init__(self, estado = ["⬜"] * 9, jogador_turno = None):
    super().__init__(estado, jogador_turno)

  def inicializar_jogadores(self):
    (humano, agente) = (JogadorVelhaHumano("❌"), JogadorAgente("🔵"))
    humano.define_proximo_turno(agente)
    agente.define_proximo_turno(humano)

    self.jogador_turno = humano

    return (humano, agente)

  def turno(self):
    return self.jogador_turno
  
  def jogar(self, jogada):
    novo_estado = self.estado.copy()
    novo_estado[jogada.posicao_quadrante] = self.jogador_turno.imprimir()
    return JogoVelha(novo_estado, self.jogador_turno.proximo_turno())

  def gerar_jogadas_validas(self):
    return [JogadaVelha(quadrante) for quadrante in range(len(self.estado)) if self.estado[quadrante] == "⬜"]
  
  def venceu(self):
    return self._venceu_linhas(self.estado) or \
    self._venceu_colunas(self.estado) or \
    self._venceu_diagonal(self.estado)
  
  def imprimir_jogada(self, jogador, jogada):
    return f"{jogador.imprimir()} jogou {jogada.posicao_quadrante + 1} ({self.estado[jogada.posicao_quadrante]})"
  
  def imprimir(self):
    return f"""{self.estado[0]}|{self.estado[1]}|{self.estado[2]}
---------
{self.estado[3]}|{self.estado[4]}|{self.estado[5]}
---------
{self.estado[6]}|{self.estado[7]}|{self.estado[8]}"""

  def calcular_utilidade(self, jogador):
    if self.venceu() and jogador.e_min():
      return -1
    elif self.venceu() and jogador.e_max():
      return 1
    else:
      return 0
    
  #######################################
  #### Funções auxiliares - privadas ####
  #######################################

  # linhas iguais e não é "⬜"
  def _venceu_linhas(self, estado):
    e = estado
    return e[0] == e[1] and e[0] == e[2] and e[0] != "⬜" or \
      e[3] == e[4] and e[3] == e[5] and e[3] != "⬜" or \
      e[6] == e[7] and e[6] == e[8] and e[6] != "⬜"

  # colunas iguais e não é "⬜"
  def _venceu_colunas(self, e):
    return e[0] == e[3] and e[0] == e[6] and e[0] != "⬜" or \
      e[1] == e[4] and e[1] == e[7] and e[1] != "⬜" or \
      e[2] == e[5] and e[2] == e[8] and e[2] != "⬜"

  # diagonal iguais e não é "⬜"
  def _venceu_diagonal(self, e):
    return e[0] == e[4] and e[0] == e[8] and e[0] != "⬜" or \
      e[2] == e[4] and e[2] == e[6] and e[2] != "⬜"
