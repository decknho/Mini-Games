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
