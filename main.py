from jogos import *
while True:
    print('[ 1 ] - Pedra, Papel ou Tesoura\n'
          '[ 2 ] - Par ou impar\n'
          '[ 3 ] - Adivinhe um numero\n'
          '[ 4 ] - Jogo da velha'
          '[   ] - Em breve\n'
          '[ 5 ] - Finalizar programa')
    minigame = int(input('Qual mini-game você deseja jogar? '))
    if minigame == 1:
        ppt()
    if minigame == 2:
        par_imp()
    if minigame == 3:
        adivinhe()
    if minigame == 4:
        jogo_velha()
    if minigame == 5:
        break
