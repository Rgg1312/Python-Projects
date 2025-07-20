print('Escolha uma operação matematica: \n+ para soma \n- para subtração \n* para multiplicação \n/ para divisão')
sinal = str(input('Digite: '))

if sinal == '+':
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))

elif sinal == '-':
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    print('{} - {} = {}'.format(numero1, numero2, numero1 - numero2))

elif sinal == '*':
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    print('{} * {} = {}'.format(numero1, numero2, numero1 * numero2))

elif sinal == '/':
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    print('{} / {} = {}'.format(numero1, numero2, numero1 / numero2))

else:
    print('\nSinal inválido!')
