def leia_int(n):
    while not n.isnumeric():
        print('\033[31mPor favor, digite somente numero...\033[m')
        n = leia_int(input('Digite um numero? '))
    return int(n)