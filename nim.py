from jogo import Jogo

class Nim(Jogo):
  def __init__(self, posicao = [10], turno = "🧑"):
    self.posicao = posicao
    self._turno = turno

  def turno(self):
    return self._turno
  
  def jogar(self, jogada):
    temp = self.posicao.copy()
    del temp[jogada[0]] # remove a pilha que o usuário escolheu
    temp.append(jogada[1])
    temp.append(jogada[2])
    if self._turno == "🧑":
      return Nim(temp, "🤖")
    else:
      return Nim(temp, "🧑")

  def gerar_jogos_validos(self):
    # para cada item da pilha self.posicao
    # se verifica se é divisível
    # gera duas pilhas de tamanhos diferentes
    # adiciona na lista de jogos válidos
    jogos_validos = []
    for torre in range(len(self.posicao)):
      for i in range(1, (self.posicao[torre] // 2) + 1):
        if (i != self.posicao[torre]-i): # corrigir por aqui
          jogos_validos.append((torre, i, self.posicao[torre]-i))
    return jogos_validos
  
  def venceu(self):
    return len(self.gerar_jogos_validos()) == 0
  
  def capturar_jogada_humano(self):
    # capturo a entrada do teclado o número da pilha e a posição que o usuário deseja partilhar esta pilha e retorno a escolha do usuário
    jogada = (-1, 0,0)
    pilha = -1
    while pilha not in range(len(self.posicao)):
      pilha = int(input("Escolha uma pilha (1-"+ str(len(self.posicao)) +"): "))
      pilha = pilha - 1
    valor = int(input("Escolha um valor (1-"+ str(self.posicao[pilha]) +"): "))
    jogada = (pilha, valor, self.posicao[pilha]-valor)
    if jogada[1] == jogada[2] and jogada[2] != 1 and jogada[1] != 1:
      print("Jogada inválida!")
    return jogada
  
  def imprimir_jogada(self, turno, jogada):
    return f"{turno} escolheu a pilha {str(jogada[0]+1)} e partilhou em ({str(jogada[1])},{str(jogada[2])})"

  def imprimir(self):
    return f"""Tabuleiro:
{self.posicao}"""

  def calcular_utilidade(self, jogador):
    if self.venceu() and self._turno == jogador:
      return -1
    elif self.venceu() and self._turno != jogador:
      return 1
    else:
      return 0