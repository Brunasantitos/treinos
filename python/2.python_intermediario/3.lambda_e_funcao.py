#lambda geralmente sao para coisas rapidas e faceis
#pode passar *args para lambda
def executa(funcao,*args):
    return funcao(*args)

def soma(x,y): #e a mesma coisa da linha 15
    return x+y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero *multiplicador
    return multiplica

#essa funcao acima, em lambda seria assim

#duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2 #esse numero no caso e o valor do parametro da funcao cria_multiplicador
)

print(duplica(2))


print(
    executa(
        #lambda x, y : x+ y, #e a mesma coisa da linha 4
        #2, 3

        lambda *args: sum(args),
        4,1
    ),
)