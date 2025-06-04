import os

def main():
   
   palavra_secreta = 'felicidade'
   letras_acertadas = ''
   numero_tentativas = 0
   while True:
    palavra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(palavra_digitada) > 1:
        print("Digite apenas uma letra")
        continue
    
    if palavra_digitada in palavra_secreta:
       letras_acertadas += palavra_digitada
       

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
          palavra_formada += letra_secreta
        else:
           palavra_formada += '*'
    print('Palavra formada: ',palavra_formada)

    if palavra_formada == palavra_secreta:
       os.system('cls') #modulo integrado, limpeza de terminal
       print("VOCÊ GANHOU, PARABÉNS!!")
       print('A palavra era: ', palavra_secreta)
       print('Tentativas: ', numero_tentativas)
       letras_acertadas = ''
       numero_tentativas = 0
          
        
if __name__=='__main__':
    main()

   

