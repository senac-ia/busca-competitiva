from minimax import minimax, minimax_alfabeta

class Jogador:
  def __init__(self, identificador):
    self.identificador = identificador

  def define_proximo_turno(self, proximo_turno):
    self.jogador_proximo_turno = proximo_turno

  def imprimir(self):
    return self.identificador
  
  def jogar(self, jogo):
    raise NotImplementedError("Deve ser implementado")
  
  def proximo_turno(self):
    return self.jogador_proximo_turno

class JogadorHumano(Jogador):
  pass

class JogadorAgente(Jogador):
  def jogar(self, jogo):
    profundidade_maxima = 8
    melhor_valor = float("-inf")
    melhor_jogada = -1
    for proximo_jogo in jogo.gerar_jogos_validos():
      utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo), False, jogo.turno(), profundidade_maxima)
      if utilidade > melhor_valor:
        melhor_valor = utilidade
        melhor_jogada = proximo_jogo
    return melhor_jogada

class Jogador:
  def oposto(self):
    raise NotImplementedError("Deve ser implementado")

class Jogo():
  def turno(self):
    raise NotImplementedError("Deve ser implementado")

  def jogar(self, localizacao):
    raise NotImplementedError("Deve ser implementado")

  def gerar_jogos_validos(self):
    raise NotImplementedError("Deve ser implementado")

  def venceu(self):
    raise NotImplementedError("Deve ser implementado")

  def empate(self):
    return (not self.venceu()) and (len(self.gerar_jogos_validos()) == 0)

  def calcular_utilidade(self, jogador):
    raise NotImplementedError("Deve ser implementado")

  def imprimir(self):
    raise NotImplementedError("Deve ser implementado")

  def imprimir_jogada(self, turno, jogada):
    raise NotImplementedError("Deve ser implementado")