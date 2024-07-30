print("\n= CALCULADORA =")

#INTERAÇÃO COM O USUÁRIO
n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#ADIÇÃO
if (n1 + n2):
    adicao = n1 + n2
    print('\nO resultado da adiçao entre',n1,'e',n2,'é:',adicao)

#SUBTRAÇÃO
if (n1 - n2):
    subtracao = n1 - n2
    print('\nO resultado da subtração entre',n1,'e',n2,'é:',subtracao)

#MULTIPLICAÇÃO
if (n1 * n2):
    multiplicacao = n1 * n2
    print('\nO resultado da multiplicação entre',n1,'e',n2,'é:',multiplicacao)

#DIVISÃO
if (n1 / n2):
    divisao = n1 / n2
    print('\nO resultado da divisão entre',n1,'e',n2,'é:',divisao)