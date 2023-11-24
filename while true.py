num = int(input('Digite um numero: '))

if num % 2 == 0:
    print('Este numero e par ')
else:
    print('Este numero e impar ')

idade = int(input('Digite sua idade: '))

if idade >= 65:
    print('Você tem gratuidade no transporte ')
else:
    print('Você não tem idade pra gratuidade no transporte ')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media > 7:
    print('Aprovado')
elif media < 5:
    print('Reprovado')
else:
    print('Recuperação')

idade = int(input('Digite sua idade: '))
modelo_oculos = 200

if idade <= 10:
    desconto = modelo_oculos - (modelo_oculos * 0.1)
    print('Você vai pagar este valor de R$ {:.2f}'.format(desconto))
elif idade > 10 and idade <= 80:
    desconto = modelo_oculos - (modelo_oculos * (idade / 100))
    print('Você vai pagar este valor de R$ {:.2f}'.format(desconto))
else:
    desconto = modelo_oculos - (modelo_oculos * 0.8)
    print('Você vai pagar este valo de R$ {:.2f}'.format(desconto))


salario = float(input('Digite o salario do funcionario: '))

if salario <= 1500:
    porcentagem = 25
    aumento = (salario * .25)
    reajuste = salario + aumento
elif salario > 1500 and salario <= 1999.99:
    porcentagem = 20
    aumento = (salario * .20)
    reajuste = salario + aumento
elif salario > 1999.99 and salario <= 2999.99:
    porcentagem = 15
    aumento = (salario * .15)
    reajuste = salario + aumento
elif salario > 2999.99 and salario <= 4999.99:
        porcentagem = 10
        aumento = (salario * .10)
        reajuste = salario + aumento
elif salario >= 5000.00:
    porcentagem = 5
    aumento = (salario * .5)
    reajuste = salario + aumento

print('1. Salario atual: R$ {:.2f}'.format(salario))
print('2. A porcentagem de reajuste: {:.0f}%'.format(porcentagem))
print('3. O aumento em R$ {:.2f}'.format(aumento))
print('4. O salario final após o reajuste R$ {:.2f}'.format(reajuste))