#Exercício de perguntas e respostas com utilização de dicionário

# conjunto de dicionario
perguntas = [ 
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51','20'],
        'Resposta': '25',
    },
    {

        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '5',
    },
    
]

qtd_acertos = 0

# esse loop acessa o questionario de cada pergunta, acessa o valor do indice Pergunta do dcionário Perguntas
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções'] #variavel 
    for i, opcao in enumerate(opcoes): #enumera os valores do indice Opcoes
        print(f'{i})',opcao) #imprime a enumeracao e os valores do indice Opcoes
    print()

    escolha = input('Escolha uma opção: ') #solicitacao de entrada para o usuario

    acertou = False 
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit(): #verifica o valor de entrada sao digitos de 0 a 9
        escolha_int = int(escolha) #transforma o valor de entrada str para int

    if escolha_int is not None: #condicona a varivael se retornar True
        if escolha_int >= 0 and escolha_int < qtd_opcoes: #verifica se a variavel e maior que 0 
            if opcoes[escolha_int] == pergunta['Resposta']: #verifica se os valores de entrada estao corretos com a resposta
                acertou = True

    if acertou: #imprime o resultado
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou')
         
print('Você acertou', qtd_acertos) #imprime no final do codigo a quantidade de acertos
print('de', len(perguntas), 'perguntas.')
