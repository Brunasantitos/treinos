#list comprehension e uma forma rapida de criar listas
#print(list(range(10)))

#em vez de ser assim
"""
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
"""

lista = [
    numero *2
    for numero in range(10)
]

print(lista)