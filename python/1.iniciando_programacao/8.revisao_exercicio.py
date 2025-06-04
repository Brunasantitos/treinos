nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
idade1 = int(idade)

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print("Seu nome contem espaço")
    else:
        print("Seu nome não contem espaço")
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe você deixou campos vazios")
