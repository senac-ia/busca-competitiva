from jogo import Jogo

class JogoVelha(Jogo):
    def __init__(self, posicao = [" "] * 9, turno = "X"):
      self.posicao = posicao
      self._turno = turno

    def turno(self):
      return self._turno
    
    def jogar(self, local):
      temp = self.posicao.copy()
      temp[local] = self._turno
      return JogoVelha(temp, "O")

    def gerar_jogos_validos(self):
      return [p for p in range(len(self.posicao)) if self.posicao[p] == " "]
    
    def venceu(self):
      return self._venceu_linhas(self.posicao) or \
      self._venceu_colunas(self.posicao) or \
      self._venceu_diagonal(self.posicao) 

     # linhas igual e não é " "
    def _venceu_linhas(self, posicao):
      return posicao[0] == posicao[1] and posicao[0] == posicao[2] and posicao[0] != " " or \
        posicao[3] == posicao[4] and posicao[3] == posicao[5] and posicao[3] != " " or \
        posicao[6] == posicao[7] and posicao[6] == posicao[8] and posicao[6] != " "

    # colunas igual e não é " "
    def _venceu_colunas(self, posicao):
      return posicao[0] == posicao[3] and posicao[0] == posicao[6] and posicao[0] != " " or \
        posicao[1] == posicao[4] and posicao[1] == posicao[7] and posicao[1] != " " or \
        posicao[2] == posicao[5] and posicao[2] == posicao[8] and posicao[2] != " "

    # diagonal igual e não é " "
    def _venceu_diagonal(self, posicao):
      return posicao[0] == posicao[4] and posicao[0] == posicao[8] and posicao[0] != " " or \
        posicao[2] == posicao[4] and posicao[2] == posicao[6] and posicao[2] != " "

    def calcular_utilidade(self, jogador):
      if self.venceu() and self._turno == jogador:
        return -1
      elif self.venceu() and self._turno != jogador:
        return 1
      else:
        return 0

    def __str__(self):
      return f"""{self.posicao[0]}|{self.posicao[1]}|{self.posicao[2]}
-----
{self.posicao[3]}|{self.posicao[4]}|{self.posicao[5]}
-----
{self.posicao[6]}|{self.posicao[7]}|{self.posicao[8]}"""