#Todos calculos fácil
print('TELA DE CONTAGEM')
a = int(input ('Digite qualquer valor:'))
b = int(input ('Digite qualquer valor:'))
print(type(a))
soma = a + b
subtracao = a - b
mutiplicacao = a * b
divisao = a / b
resto = a % b
print('soma: {}' .format(soma))
print('subtracao: {}' .format(subtracao))
print('multiplicacao: {}' .format(mutiplicacao))
print('divisao: {}' .format(divisao))

#calculo maior que

print('resto:{}' .format(resto))
print('TELA DE MAIOR NÚMERO')
if a > b:
        print('o maior número é {}' .format(a))

else:
        print('o maior número é {}' .format(b))

#Para mostrar se é par ou impar
a = int(input('Entre com um valor'))
resto = a % 2
if resto == 0:
    print('Número é par')
else:
    print('Número é impar')


print('FINAL DO PROGRAMA')