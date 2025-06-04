'''
for in é uma estrutura de repetição que tem um, a mesma não precisa de um contador como a estrutura while
'''

letra = "bruna"

for i in letra:
    print(letra)
    
print(35*'_')
'''
exemplo para enumerar texto:
'''

for n, i in enumerate(letra): # in (em)
    print(n, i)


print(35*'_')
'''
funcionalidade de RANGE em FOR
'''
#a funcionalidade RANGE e FOR, não dependem uma da outra

for i in range(20, 50, 2): #range(start, stop, step)
    print(i)


'''
UTILIZAÇÃO: continue, break
'''

#continue: pula para o próximo laço

#termina o laço

print(35*'_')

#EXEMPLO DE CONTINUE E BREAK COM O LAÇO FOR:


nome = 'bruna1'
espaco = ''

for i in nome:
    if i == 'b':
        espaco += i.upper()
        continue
    elif i == 'r':
        espaco += i
        continue
    elif i == 'u':
        espaco += i
        continue
    elif i == 'n':
        espaco += i.upper()
        continue
    elif i == 'a':
        espaco += i
        print(espaco)
        break  #para verificar a condição de continue nessa logica, é só mudar o break para "continue"
    elif i == '1':
        print("testanto iterador")
