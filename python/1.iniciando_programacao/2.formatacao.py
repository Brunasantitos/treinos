#formatações :d(inteiro), :s(string), :f(float), :.(casas decimais)
#<(a direita), >(a esquerda), ^(espaco entre)
#.format() e ljust()
#tem muitas funções após o (.)

a = 5
b = 'b'
c = 'bruna'

print('{:s}' .format(b))
print('{:f}' .format(a))

bruna = '{:@>6}' .format(c)
print(bruna) #tem que ser maior do que os caracteres em strings
print('{:@>6}' .format(c))

print(f'{c: ^7}')#tem que ser maior do que os caracteres em strings




