'''
digito1, digito2, digito3 = 7,4,6
digito4, digito5, digito6 = 8,2,4
digito7, digito8, digito9 = 8,9,0

multiploD1 = digito1 * 10
multiploD2 = digito2 * 9
multiploD3 = digito3 * 8
multiploD4 = digito4 * 7 
multiploD5 = digito5 * 6
multiploD6 = digito6 * 5
multiploD7 = digito7 * 4
multiploD8 = digito8 * 3
multiploD9 = digito9 * 2

somaTudo = multiploD1+multiploD2+multiploD3+multiploD4+multiploD5+multiploD6+multiploD7+multiploD8+multiploD9
multiploResultado = (somaTudo * 10) % 11

if multiploResultado <= 9:
    print(f'{multiploResultado}')
else:
    print(0)
'''

#RESOLUÇÃO PROFESSOR
def primeiroDigito(cpf,resultadoDigito):
    
    noveDigitos = cpf[:9]
    contadorRegressivo = 10
    
    for digito in noveDigitos:
        resultadoDigito += int(digito) * contadorRegressivo
        contadorRegressivo -= 1
    digito = (resultadoDigito * 10) % 11
    digito = digito if digito <= 9 else 0 
    # lê-se DIGITO RECEBE DIGITO SE DIGITO FOR MENOR OU IGUAL A 9, O CONTRÁRIO RECEBERÁ 0
    return digito

def segundoDigito(cpf,resultadoDigito):
    dezDigitos = cpf[:10]
    contadorregressivo = 11

    for digito in dezDigitos:
        resultadoDigito += int(digito)*contadorregressivo
        contadorregressivo-=1
    digito2 = (resultadoDigito*10)%11
    digito2 = digito2 if digito2 <= 9 else 0
    return digito2

#corrigir validação
def validacaoCPF(digito1,digito2,cpf):
    ultimosNumeros =cpf[-2:]
   
    if str(digito1)+str(digito2) != ultimosNumeros:
        print(f'CPF {cpf} válido!')
    else:
        print('CPF inválido!')
    
def main():
    cpf = '06169920335'
    resultadoDigito = 0
    primeiroDigito(cpf,resultadoDigito)
    segundoDigito(cpf,resultadoDigito)
    validacaoCPF(primeiroDigito,segundoDigito,cpf)

if __name__=='__main__':
    main()