lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

#lista comprehension
#o lado esquerdo do for e usado para mapeamento
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)
