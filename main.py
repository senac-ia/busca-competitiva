from jogo_velha import JogoVelha

if __name__ == "__main__":
  jogo = JogoVelha()

  while True:
    humano = jogo.capturar_jogada_humano()
    jogo = jogo.jogar(humano)
    if jogo.venceu():
      print("Humano Venceu!")
      break
    elif jogo.empate():
      print("Empate!")
      break

    computador = jogo.capturar_jogada_agente()
    print(f"Jogada do Computador é {computador}")
    jogo = jogo.jogar(computador)
    print(jogo.imprimir())

    if jogo.venceu():
      print("Computador venceu!")
      break
    elif jogo.empate():
      print("Empate!")
      break