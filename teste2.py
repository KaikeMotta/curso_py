
sair = None
funcionarios = []
posiçao = 0

while sair == None:
    sair = input('Digite [0] para sair: ')
       
    if sair == "0":
        break
    
while sair != "0":
    posiçao += 1
    funcionario = input(f'funcionario {posiçao}: ')
    funcionarios.append(funcionario)
    
    
    if funcionario == "0":
        print(f'funcionarios:{funcionarios}')
        break
    
    continue


        
        


        
        
    
    
   


    
   