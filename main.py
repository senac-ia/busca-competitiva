import time
from jogo_velha import JogoVelha
from nim import Nim

if __name__ == "__main__":
  jogo = JogoVelha()
  (jogador_humano, jogador_agente) = jogo.inicializar_jogadores()

  print("Situação do Jogo:")
  print(jogo.imprimir())
  print("=======================================")

  while True:
    # Turno no humano
    jogada_humano = jogador_humano.jogar(jogo)
    print(jogo.imprimir_jogada(jogador_humano, jogada_humano))
    print("=======================================")
    jogo = jogo.jogar(jogada_humano)
    
    if jogo.venceu():
      print(f"{jogador_humano.imprimir()} Venceu!")
      break
    elif jogo.empate():
      print("Empate!")
      break

    # Turno no agente
    print("Situação do Jogo:")
    print(jogo.imprimir())
    print("=======================================")

    # Dorme um pouco para dar um efeito de pensar
    print(f"{jogador_agente.imprimir()} está pensando...")
    time.sleep(5)

    jogada_agente = jogador_agente.jogar(jogo)
    print(jogo.imprimir_jogada(jogador_agente, jogada_agente))
    print("=======================================")
    jogo = jogo.jogar(jogada_agente)
    
    print(jogo.imprimir())

    if jogo.venceu():
      print(f"{jogador_agente.imprimir()} venceu!")
      break
    elif jogo.empate():
      print("Empate!")
      break

  print(jogo.imprimir())