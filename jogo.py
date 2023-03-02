class Jogador:
  def oposto(self):
      raise NotImplementedError("Deve ser implementado")

class Jogo():
  def turno(self):
    pass

  def jogar(self, localizacao):
    pass

  def gerar_jogos_validos(self):
    pass

  def venceu(self):
    pass

  def empate(self):
    return (not self.venceu()) and (len(self.gerar_jogos_validos()) == 0)

  def capturar_jogada_agente(self, jogador):
    pass

  def capturar_jogada_humano(self):
    pass

  def calcular_utilidade(self, jogador):
    pass