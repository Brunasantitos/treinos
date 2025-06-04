'''
LISTAS: guarda vários valores de diferentes tipos
VARIAVEIS: guarda apenas um valor especifico
'''
# fatiamento de listas

lista = ['a', 'b', 'c', 'd', 'e', 10]

print(lista[::2]) # mesma lógica de fatiamento de strings

'''
VALORES:
append(insere um novo valor no final da lista),
insert(insere um novo valor),
pop(deleta um argumento da lista),
del(apaga da lista mais de um argumento),
clear,
extend(mesma utilização do append)
'''

lista2 = [1, 2, 3, 4, 5]
print(lista)


lista.extend(lista2) # adiciona o argumento no final da lista
print(lista)


lista.append('158') # adiciona o argumento no finla da lista
print(lista)


lista.insert(1,54) # o primeiro número é para informar em qual índice o argumento se localizará
print(lista)


lista.pop(3) # apaga um argumento da lista, caso queira apagar um argumento específico, coloca apenas o índice do dado
print(lista)


lista3 = [1, 2, 3, 4, 5, 6] # apaga mais de um argumento de uma vez, basta colocar os índices que queira apagar
del(lista3[2:5])
print(lista3)
