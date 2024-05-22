while True:
    
    valor1 = input("Digite o valor 1: ") 
    valor2 = input("Digite o valor 2: ")

    valor_very = None
    try:
        valor1_floot = float(valor1)
        valor2_floot = float(valor2)
        valor_very = True

    except ValueError:
        print('O valor 1 ou valor 2 esta incoreto!!!')

    
    if valor_very is True:
        resultado = print(valor1_floot + valor2_floot ) 
    
    
    sair = input('Deseja parar ? [S]im : ')

    if sair == 'S':
        break   
    else: 
        continue




  


    
    
    
    

   

    
        
     

     