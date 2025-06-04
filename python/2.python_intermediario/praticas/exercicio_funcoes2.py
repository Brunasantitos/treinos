def multiplicar(multiplicador):
    def duplicar(numero):
        return numero*multiplicador
    return duplicar
    
def main():
    valor_1=multiplicar(2)
    valor_2=multiplicar(3)
    valor_3=multiplicar(4)

    print(valor_1(5))
    print(valor_2(8))
    print(valor_3(8))

if __name__=='__main__':
    main()