def manipulandoListas():
    listaCompras = []
    while True:
        print("Escolha as seguintes opções\n1-Adicionar Item\n2-Apagar Item\n3-Verificar Itens\n4-Sair")
        
        try:
            valorEntrada = int(input("Informe a sua escolha: "))

            if valorEntrada == 1:
                    
                intemAdicionado = input("Digite o item que queira adicionar: ")
                listaCompras.append(intemAdicionado)    
                print(f'\nItem adicionado, {listaCompras}')

            elif valorEntrada == 2:
                if listaCompras:
                    print(listaCompras)
                    excluirItem = input("Digite o item que deseja excluir: ")
                    if excluirItem in listaCompras:
                        listaCompras.remove(excluirItem)
                        print(f'\nCONFERINDO LISTA {listaCompras}')
                    else:
                        print("Item não encontrado!")
                else:
                    print("\nLista vazia!")
                
            elif valorEntrada == 3:
                if listaCompras:
                    print(f'\nProdutos que já foram adicionados\n{listaCompras}')
                else:
                    print("\nLista Vazia!")

            elif valorEntrada == 4:
                indicesListas = len(listaCompras)
                if indicesListas == 0 :
                    print("Lista vazia!")
                else:
                    listaTupla = tuple(listaCompras)
                    print(f'SUA LISTA DE COMPRAS\n{listaTupla}')
                break

        except ValueError:
            print("\nInforme apenas número!")

def main():
    manipulandoListas()

if __name__=='__main__':
    main()
