from jogos import *
while True:
      print('[ 1 ] - Pedra, Papel ou Tesoura\n'
            '[ 2 ] - Par ou impar\n'
            '[ 3 ] - Adivinhe um numero\n
            '[   ] - Em breve\n'
            '[ 4 ] - Finalizar programa')
      minigame = int(input('Qual mini-game você deseja jogar? '))
      if minigame == 1:
            ppt()
      if minigame == 2:
            par_imp()
      if minigame == 3:
            adivinhe()
      if minigame == 4:
            break
