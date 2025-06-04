def retorno_multiplicado(*args):
    total = 1
    for multiplicados in args:
        total *= multiplicados
        print(multiplicados, total)
       
def impar_par(numero):

    if (numero%2)==0:
        return 'Número {numero} é par'
        
    return 'Número {numero} é ímpar'


def main():
    retorno_multiplicado(160,4,8,7)
    print(impar_par(8))
    print(impar_par(7))

if __name__=='__main__':
    main()