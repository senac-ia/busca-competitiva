from jogo import Jogo
from minimax import melhor_jogada_agente

class JogoVelha(Jogo):
  def __init__(self, posicao = ["⬜"] * 9, turno = "❌"):
    self.posicao = posicao
    self._turno = turno

  def turno(self):
    return self._turno
  
  def jogar(self, local):
    temp = self.posicao.copy()
    temp[local] = self._turno
    if self._turno == "❌":
      return JogoVelha(temp, "🔵")
    else:
      return JogoVelha(temp, "❌")

  def gerar_jogos_validos(self):
    return [p for p in range(len(self.posicao)) if self.posicao[p] == "⬜"]
  
  def venceu(self):
    return self._venceu_linhas(self.posicao) or \
    self._venceu_colunas(self.posicao) or \
    self._venceu_diagonal(self.posicao)
  
  def capturar_jogada_humano(self):
    jogada = -1
    while jogada not in self.gerar_jogos_validos():
      jogada = int(input("Escolha um quadrado (1-9):"))
      jogada -= 1 # 1-9 -> 0-8
    return jogada
  
  def capturar_jogada_agente(self):
    return melhor_jogada_agente(self)
  
  def imprimir(self):
    return f"""{self.posicao[0]}|{self.posicao[1]}|{self.posicao[2]}
---------
{self.posicao[3]}|{self.posicao[4]}|{self.posicao[5]}
---------
{self.posicao[6]}|{self.posicao[7]}|{self.posicao[8]}"""

  def calcular_utilidade(self, jogador):
    if self.venceu() and self._turno == jogador:
      return -1
    elif self.venceu() and self._turno != jogador:
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
