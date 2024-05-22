while True:
    
    palavra_secreta = len("kaike")

    usuario = input('digite um palavra: ')

    verificar_se_1letra = len(usuario)

    if verificar_se_1letra > 1:
        print("voce digitou mais de caracter por vez")
        continue
    
    if len(usuario) == palavra_secreta:
        palavra = len(usuario)
        print(palavra)
        
    
    