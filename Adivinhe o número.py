import random
num = random.randint(1, 100)
contador = 1

while True:
    num2 = int(input('\nDigite um número: '))
    if num2 == num:
        print('\nVocê conseguiu! Você acertou em {} tentativa(s)'.format(contador))
        break
    else:
        contador = contador + 1
        if num2 < num:
            print('\nMaior...')
        elif num2 > num:
            print('\nMenor...')
