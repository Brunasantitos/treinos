# dir tras todos os nomes definidos dentro de str
# hasattr checa se determinado objeto tem um determinado nome dentro 
# getattr 
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)