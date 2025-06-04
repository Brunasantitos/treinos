# Digitar um caractere do tipo inteiro, retornar se é ímpar ou par. O contrário informar ao usuário que não é do tipo int

def numero(n):
    if n.isdigit():
        n = int(n)
        
        if n % 2 == 0:
            print("Seu número é par.")
        elif n != 0:
            print("Seu número é ímpar.")
    else:
        print("Seu caractere não é do tipo inteiro.")

# programação ao contrário
'''
def oContratio(n):

    if not n.isdigit():
        print("Seu caractere não é do tipo inteiro.")

    else:
        n = int(n)

        if n % 2 == 0:
            print("Seu número é par.")
        elif n != 0:
            print("Seu número é ímpar.")
'''

#informar um horário:
#Bom dia(0-11), Boa tarde(12-17) e Boa noite(18-23)
def horario(hr):
    if hr <= 11:
        print("Bom dia")
    elif hr <= 17:
        print("Boa tarde")
    else:
        print("Boa noite")

#pedir o primeiro nome do usuário. se o nome tiver 4 letras ou menos: "seu nome é curto"
#se tiver entre 5 e 6 letras:"seu nome é normal", maior que 6:"seu nome é muito grande"
def nome(primeiro_nome):
    if len(primeiro_nome) <= 4:
        print("Seu nome é curto!")
    elif len(primeiro_nome) <=6:
        print("Seu nome é normal!")
    else:
        print("Seu nome é muito grande!")

def main():
    n = input("Informe um número para saber se é par ou ímpar: ")
    numero(n)
    #oContratio(n)
    
    hr = float(input("\nQua horas são? "))
    horario(hr)

    primeiro_nome = input("\nInforme o seu primeiro nome ")
    nome(primeiro_nome)

    
if __name__=='__main__':
    main()



