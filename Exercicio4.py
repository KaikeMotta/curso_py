nome = input('Digite seu nome: ')
idade = input('digite sua idade: ')

print(30*'-')

if nome and idade:
 print(f'Seu nome: {nome}') 
  
 if ' ' in nome:
    print('seu nome contem espaço')
 else:
    print('seu nome nao contem espaço')

 print(f'Seu nome invertido: {nome[ : :-1]}')
 print(f'Seu nome tem: {len(nome)}')
 print(f'A primeira letra do seu nome é: {nome[0]}')
 print(f'A ultima letra do seu nome é: {nome[-1]}')

else :

 print('Voce nao digitou nada')




