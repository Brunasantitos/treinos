peca1 = input().split()
codigo1, numero1, valor1 = int(peca1[0]), int(peca1[1]), float(peca1[2])
peca2 = input().split()
codigo2, numero2, valor2 = int(peca2[0]), int(peca2[1]), float(peca2[2])
valorPeca = ((numero1 * valor1) + (numero2 * valor2))
print(f'VALOR A PAGAR: R$ {valorPeca:.2f}')