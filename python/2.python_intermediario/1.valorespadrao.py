'''
Os parâmetros podem ter valores padrão.
o 0 é considerado por padrão, como FALSE, assim não retornando nada.
Exemplo abaixo como inverter essa situação.
'''

def soma(x,y,z=None): #para o z ser impresso, tendo o valor 0, colocamos None
    if z is not None:
        print(f'{x=} {y=} {z=}', x+y+z)
    else:
        print(f'{x=} {y=}', x+y)

soma(1,2)
soma(3,5,0)