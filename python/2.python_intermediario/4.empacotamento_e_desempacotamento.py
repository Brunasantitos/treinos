# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
#a, b = b, a
print(a, b)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

#a,b = pessoa.values() #retorna os valore do dicionario
#print(a,b)


#(a1,a2), (b1, b2), = pessoa.items()
#print(a1,a2)
#print(b1,b2)

#for chave, valor in pessoa.items(): #retorna a chave e o valor do dicionario
   # print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

#extrai dentro de um dicinario as informacoes do outro dicionario
pessoas_completa = {
    **pessoa,
    'chave': 1,
    **dados_pessoa,
    'nome': 2
}

print(pessoa, dados_pessoa)

#kwargs - keyword arguments

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='joana', qlq=123456)
#desempacotando o kwargs
mostro_argumentos_nomeados(**pessoas_completa)