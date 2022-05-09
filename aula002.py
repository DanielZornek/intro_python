a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o Segundo Valor: '))
soma = a + b
subtrair = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(type(soma)) # verificando o tipo de uma variavel #
soma = str(soma)
# convertendo soma para uma string
print(type(soma))
print('soma : ' + soma)
print(soma)

print('Subtração: ' + str(subtrair))

print(multiplicacao)
# Outra maneira de converter
print('Multiplicação: {} '.format(multiplicacao))

print(divisao)

print(resto)

print(' Soma: {} \n Subtração {} '.format(soma, subtrair))

print("\nImprimindo Tudo!!!")

resultado = ( '\nSoma: {soma} \n Subtração: {sub} \n Multiplicação: {multi} \n Divisão: {divi} \n Resto: {rest}'.format
       (soma= soma, sub=subtrair, multi=multiplicacao, divi=divisao, rest=resto ) )

print(resultado)