from minimax import minimax, minimax_alfabeta

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

  def capturar_jogada_agente(self):
    profundidade_maxima = 8
    melhor_valor = float("-inf")
    melhor_jogada = -1
    for proximo_jogo in self.gerar_jogos_validos():
      utilidade = minimax_alfabeta(self.jogar(proximo_jogo), False, self.turno(), profundidade_maxima)
      if utilidade > melhor_valor:
        melhor_valor = utilidade
        melhor_jogada = proximo_jogo
    return melhor_jogada

  def capturar_jogada_humano(self):
    pass

  def calcular_utilidade(self, jogador):
    raise NotImplementedError("Deve ser implementado")

  def imprimir(self):
    raise NotImplementedError("Deve ser implementado")

  def imprimir_jogada(self, turno, jogada):
    raise NotImplementedError("Deve ser implementado")