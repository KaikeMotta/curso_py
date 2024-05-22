while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos or len(operador) != 1:
        print('Operador inválido.')
        continue

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
    
    
    

        

        
    

