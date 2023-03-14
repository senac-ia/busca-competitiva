from jogo import Jogo, JogadorHumano, JogadorAgente, Jogada

class JogadaNim(Jogada):
  def __init__(self, pilha, valor1, valor2):
    self.pilha = pilha
    self.valor1 = valor1
    self.valor2 = valor2

  def valores(self, pilha, valor1, valor2):
    self.pilha = pilha
    self.valor1 = valor1
    self.valor2 = valor2

  def e_valida(self):
    return self.valor1 != self.valor2 and \
      self.valor2 != 1 and self.valor1 != 1 and \
      self.pilha >= 0

class JogadorNimHumano(JogadorHumano):
  # capturo a entrada do teclado o número da pilha e a 
  # posição que o usuário deseja partilhar esta pilha e retorno a escolha do usuário
  def jogar(self, jogo):
    jogada = JogadaNim(-1, 1, 1)

    while not jogada.e_valida():
      jogada.pilha  = int(input("Escolha uma pilha (1-"+ str(len(jogo.estado)) +"): ")) - 1
      jogada.valor1 = int(input("Escolha um valor (1-"+ str(jogo.estado[jogada.pilha]) +"): "))
      jogada.valor2 = jogo.estado[jogada.pilha] - jogada.valor1
    return jogada

class Nim(Jogo):
  def __init__(self, estado = [10], jogador_turno = None):
    super().__init__(estado, jogador_turno)

  def inicializar_jogadores(self):
    (humano, agente) = (JogadorNimHumano("🧑"), JogadorAgente("🤖"))
  
    humano.define_proximo_turno(agente)
    agente.define_proximo_turno(humano)

    self.jogador_turno = humano

    return (humano, agente)

  def turno(self):
    return self.jogador_turno
  
  def jogar(self, jogada):
    novo_estado = self.estado.copy()
    # remove a pilha que o usuário escolheu
    # adiciona as novas pilhas
    del novo_estado[jogada.pilha] 
    novo_estado.append(jogada.valor1)
    novo_estado.append(jogada.valor2)

    return Nim(novo_estado, self.jogador_turno.proximo_turno())

  def gerar_jogadas_validas(self):
    # para cada item da pilha self.estado
    # se verifica se é divisível
    # gera duas pilhas de tamanhos diferentes
    # adiciona na lista de jogos válidos
    jogos_validos = []
    for torre in range(len(self.estado)):
      for i in range(1, (self.estado[torre] // 2) + 1):
        if (i != self.estado[torre]-i):
          jogada = JogadaNim(torre, i, self.estado[torre]-i)
          jogos_validos.append(jogada)
    return jogos_validos
  
  def venceu(self):
    return len(self.gerar_jogadas_validas()) == 0
  
  def imprimir_jogada(self, jogador, jogada):
    return f"{jogador.imprimir()} escolheu a pilha {str(jogada.pilha+1)} e partilhou em ({str(jogada.valor1)},{str(jogada.valor2)})"

  def imprimir(self):
    return f"""Tabuleiro:
{self.estado}"""

  def calcular_utilidade(self, jogador):
    if self.venceu() and self.jogador_turno == jogador:
      return -1
    elif self.venceu() and self.jogador_turno != jogador:
      return 1
    else:
      return 0