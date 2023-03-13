import time
from jogo_velha import JogoVelha
from nim import Nim

if __name__ == "__main__":
  jogo = Nim()
  print("Situação do Jogo:")
  print(jogo.imprimir())
  print("=======================================")

  while True:
    # Turno no humano
    jogada_humano = jogo.capturar_jogada_humano()
    print(jogo.imprimir_jogada(jogo.turno(), jogada_humano))
    print("=======================================")
    jogo = jogo.jogar(jogada_humano)
    

    if jogo.venceu():
      print("Humano Venceu!")
      break
    elif jogo.empate():
      print("Empate!")
      break

    # Turno no agente
    print("Situação do Jogo:")
    print(jogo.imprimir())
    print("=======================================")

    # Dorme um pouco para dar um efeito de pensar
    time.sleep(5)

    jogada_agente = jogo.capturar_jogada_agente()
    print(jogo.imprimir_jogada(jogo.turno(), jogada_agente))
    print("=======================================")
    jogo = jogo.jogar(jogada_agente)
    
    print(jogo.imprimir())

    if jogo.venceu():
      print("Computador venceu!")
      break
    elif jogo.empate():
      print("Empate!")
      break

  print(jogo.imprimir())