#sets são eficientes para remover valores duplicados
#não aceita valores mutáveis
#não tem índexes
#não garantem prdem
#são iteráveis (for, in, not in)
'''
l1 = [1,2,1,1,1,3,5,5,6,4,8,9,1]
s1 = set(l1)

print(s1)

s2 = {1,2,3,3}
print (5 not in s2)

#métodos úteis
#add, update, clear, discard
s3 = set()
s3.add('bruna')
print(s3)
s3.add(1)
print(s3)
s3.update(('olá mundo', 3,1,5))
#s3.clear() #limpa o set
#s3.discard() #elimina apenas o valor passado
print(s3)
'''
#operadores uteis no set
#uniao | - uner
#interseccao & - itens presentes em ambos
#diferenca - itens presentes apenas no set da esquerda
#diferenca simetrica ^ - itens que nao estao em ambos
set1 = {1,2,3,4,5}
set2 = {5,4,2,3,8}
intersecao = set1 | set2
print(intersecao)
um_item = set1 & set2
print(um_item)
apenas_um_set = set1 - set2
print(apenas_um_set)
diferenca = set2 ^ set1
print(diferenca)


