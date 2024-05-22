"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#numero = input('Digite um numero inteiro: ')

'''''''''
if numero.isdigit():
    numero_int = int(numero)
    div = numero_int % 2
    
    if div == 0:
       print(f'{numero} é par')

    elif div == 1:
       print(f'{numero} é impar')

else:
    print("voce nao digitou um numero inteiro")
'''''''''

"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Escreva a hora:')

try:
    hora = int(entrada)
    
    if hora <= 11:
        print('BOM DIA')
    elif hora > 12 and hora < 17:
        print("Boa tarde")
    elif hora > 18 and hora < 23:
        print("Boa noite")

except:
    print('voce nao digitou a hora')
  

"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""






