def ppt():
    from random import randint  # numero aleatorio pro computador
    from time import sleep  # enfase
    print('\033[31m[ 1 ] Pedra\033[m\n'
          '\033[35m[ 2 ] Papel\033[m\n'
          '\033[34m[ 3 ] Tesoura\033[m')  # escolhar do usuario
    while True:
        jogada = int(input('Um numero de 1 a 3? '))  # pegando a escolha do usuario
        while True:
            if jogada != 3 and jogada != 2 and jogada != 1:
                jogada = int(
                    input('Um numero de 1 a 3? '))  # pegando a escolha do usuario novamente se for um numero invalido
            else:  # parando o while se a escolha do usuario for valida
                break
        print('Pedra...')  # enfase
        sleep(0.8)
        print('Papel...')  # enfase
        sleep(0.8)
        print('Tesoura...')  # enfase
        sleep(1.5)
        computador = randint(1, 3)  # computador escolhendo
        # computando o resultado
        if computador == jogada:
            print('Deu \033[33mEMPATE\033[m')
        elif computador < 2 < jogada:
            print('\033[31mPerdeu\033[m eu escolhi pedra')
        elif computador < jogada < 3:
            print('\033[32mGanhou\033[m eu escolhi pedra')
        elif jogada < computador < 3:
            print('\033[31mPerdeu\033[m eu escolhi papel')
        elif jogada < 2 < computador:
            print('\033[32mGanhou\033[m eu escolhi tesoura')
        elif 1 < computador < jogada:
            print('\033[32mGanhou\033[m eu escolhi papel')
        elif 1 < jogada < computador:
            print('\033[31mPerdeu\033[m eu escolhi tesoura')
        # print('Possiveis resultados da partida')
        finalizar = str(input('Deseja ir mais uma rodada [S/N] ')).upper()  # perguntando se quer finalizar o programa
        if finalizar in 'N':
            break  # programa finalizado


def par_imp():
    from random import randint
    print('\033[36mJogo do par ou impar\033[m')
    while True:
        vitorias = 0
        while True:
            computador = randint(1, 10)
            usuario = int(input('Escolha um numero de 1 a 10...'))
            print('Escolha impar ou par, "I" para impar e "P" para par ', end='')
            escolha = ' '
            while escolha not in 'PpIi':
                escolha = str(input('[I/P] ')).upper()
            total = usuario + computador
            if escolha == 'P' and total % 2 == 0 or escolha == 'I' and total % 3 == 0:
                print(
                    f'\033[32mPARABÉNS\033[m, a soma entre o numero escolhido pelo computador "{computador}" e o seu é igual a {total}')
            else:
                print(
                    f'Você \033[31mPERDEU\33[m, a soma entre o numero escolhido pelo computador "{computador}" e o seu é igual a {total}')
                break
            vitorias += 1
        print(f'\033[35mO total de vitorias seguidas foi "{vitorias}"\033[m')
        finalizar = str(input('Deseja ir mais uma rodada [S/N] ')).upper()  # perguntando se quer finalizar o programa
        if finalizar in 'N':
            break  # programa finalizado


def adivinhe():
    from random import randint
    while True:
        computador = randint(1, 10)
        print('Eu pensei em um numero de 1 a 10, tente adivinhar qual foi...')
        num = int(input('Qual foi o numero? '))
        cont = 1
        while num != computador:
            print('Numero errado, o numero é', end=' ')
            if computador < num:
                print('Menor...')
            elif computador > num:
                print('Maior...')
            num = int(input('Qual é o numero? '))
            cont += 1
        if cont == 1:
            print('Parabéns, você acertou de 1°!!')
        else:
            print(f'Acertou. Foram necessárias {cont} tentativas')
        finalizar = str(input('[ A ] - Mais uma rodada?\n'
                              '[ B ] - Finalizar\n'
                              '=> Sua escolha? ')).strip().upper()[0]
        while finalizar not in 'AB':
            print('Escolha invalida')
            finalizar = str(input('Sua escolha? ')).strip().upper()[0]
        if finalizar in 'B':
            break


def jogo_velha():
    from random import randint
    from interface import leia_int
    while True:
        rodada = str(input('O seu simbolo é "x" ou "o"? ')).strip().upper()[0]
        jogadas = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
        print(f'[{jogadas["1"]}][{jogadas["2"]}][{jogadas["3"]}]\n'
              f'[{jogadas["4"]}][{jogadas["5"]}][{jogadas["6"]}]\n'
              f'[{jogadas["7"]}][{jogadas["8"]}][{jogadas["9"]}]\n')
        jogador = list()
        computador = list()
        cont = 0
        while True:
            if rodada in 'X':
                selecaoj = int(input(f'Aonde você ira colocar o "{rodada}"? '))
                while selecaoj in jogador or selecaoj in computador:
                    print('\033[31mEssa entrada ja foi selecionada. Por favor escolha outra\033[m')
                    selecaoj = int(input(f'Aonde você ira colocar o "{rodada}"? '))
                jogadas[f"{selecaoj}"] = 'x'
                jogador.append(selecaoj)
                cont += 1
                selecaoc = randint(1, 9)
                while selecaoc in computador or selecaoc in jogador:
                    selecaoc = randint(1, 9)
                jogadas[f"{selecaoc}"] = 'o'
                computador.append(selecaoc)
                cont += 1
            if rodada in 'O':
                selecaoj = int(input(f'Aonde você ira colocar o "{rodada}"? '))
                while selecaoj in jogador or selecaoj in computador:
                    print('\033[31mEssa entrada ja foi selecionada. Por favor escolha outra\033[m')
                    selecaoj = int(input(f'Aonde você ira colocar o "{rodada}"? '))
                jogadas[f"{selecaoj}"] = 'o'
                jogador.append(selecaoj)
                cont += 1
                selecaoc = randint(1, 9)
                while selecaoc in computador or selecaoc in jogador:
                    selecaoc = randint(1, 9)
                jogadas[f"{selecaoc}"] = 'x'
                computador.append(selecaoc)
                cont += 1
            partida = (f'\033[34m[\033[m{jogadas["1"]}\033[34m]\033[m'
                       f'\033[34m[\033[m{jogadas["2"]}\033[34m]\033[m'
                       f'\033[34m[\033[m{jogadas["3"]}\033[34m]\033[m\n'
                       f'\033[34m[\033[m{jogadas["4"]}\033[34m]\033[m'
                       f'\033[34m[\033[m{jogadas["5"]}\033[34m]\033[m'
                       f'\033[34m[\033[m{jogadas["6"]}\033[34m]\033[m\n'
                       f'\033[34m[\033[m{jogadas["7"]}\033[34m]\033[m'
                       f'\033[34m[\033[m{jogadas["8"]}\033[34m]\033[m'
                       f'\033[34m[\033[m{jogadas["9"]}\033[34m]\033[m\n')
            print(partida)
            if 3 in jogador and 2 in jogador and 1 in jogador or 4 in jogador and 5 in jogador and 6 in jogador \
                    or 7 in jogador and 9 in jogador and 8 in jogador \
                    or 1 in jogador and 4 in jogador and 7 in jogador \
                    or 2 in jogador and 5 in jogador and 8 in jogador \
                    or 3 in jogador and 6 in jogador and 9 in jogador \
                    or 1 in jogador and 5 in jogador and 9 in jogador \
                    or 3 in jogador and 5 in jogador and 7 in jogador:
                print('Você \033[32mGANHOU!\033[m')
                break
            if 3 in computador and 2 in computador and 1 in computador \
                    or 4 in computador and 5 in computador and 6 in computador \
                    or 7 in computador and 9 in computador and 8 in computador \
                    or 1 in computador and 4 in computador and 7 in computador \
                    or 2 in computador and 5 in computador and 8 in computador \
                    or 3 in computador and 6 in computador and 9 in computador \
                    or 1 in computador and 5 in computador and 9 in computador \
                    or 3 in computador and 5 in computador and 7 in computador:
                print('Você \033[31mPERDEU!\033[m')
                break
            if cont == 8:
                print('\033[33mEmpate\033[m')
                break
        continuar = leia_int(input('[ 1 ] - Outra rodada\n'
                                   '[ 2 ] - Voltar ao menu\n'
                                   '=> '))
        if continuar == 2:
            break