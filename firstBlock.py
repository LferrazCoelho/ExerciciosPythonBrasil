#EXE 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

# print("Alo mundo")

#EXE 2 - Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]".

# print("Verificação de ID")
# age = int(input("Digite um numero: "))
# print("O número informado foi {}".format(age))

#EXE 3 - Faça um Programa que peça dois números e imprima a soma.

# print("Vamos somar!")
# nu1 = int(input("Digite o primeiro valor: "))
# nu2 = int(input("Digite o segundo valor: "))
# print("O resultado de {} + {} é {}".format(nu1, nu2, nu1+nu2))

#EXE 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# print("Consulte sua média bimestral")
# note1 = float(input("Digite a primeira nota: "))
# note2 = float(input("Digite a segunda nota: "))
# note3 = float(input("Digite a terceira nota: "))
# note4 = float(input("Digite a quarta nota: "))
# noteall = note1 + note2 + note3 + note4
# media = noteall/4
# print("Sua méida é {:.2f}".format(media))
# if media > 5.99:
#     print("Aprovado ;)")
# else:
#     print("Reprovado :/")

#EXE 5 - Faça um Programa que converta metros para centímetros.

# print("Convertar metros em centímetros")
# m = int(input("Digite a quantidade desejada: "))
# conver = m * 100
# if m < 2:
#     print("{} metro é igual a {} centímetros".format(m, conver))
# else:
#     print("{} metros é igual a {} centímetros".format(m, conver))

#EXE 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# import math
# print("Descubra a área do Círculo")
# radius = float(input("Digite o raio do círculo em centímetros: "))
# pi = math.pi
# circle = pi * (radius ** 2)
# print("O círculo possue uma área de {:.2f}cm".format(circle))

#EXE 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# side = float(input("Digite o tamanho em centímetros de um lado do quadrado: "))
# square = side * 2
# print("O dobro da área do quadrado é {}cm".format(square))

#EXE 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#        Calcule e mostre o total do seu salário no referido mês.

# print("Descubra o seu salário")
# money_hour = float(input("Digite em Reais, quanto vc ganha por hora: "))
# work_hour = int(input("Digite quantas horas vc trabalhou esse mês: "))
# salary = money_hour * work_hour
# print("Seu salário esse mês é {} reais".format(salary))

#EXE 9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#        C = (5 * (F-32) / 9).

# print("Vamos converter graus Farenheit, em Celsius")
# F = int(input("Qual a temperatura em Farenheit? "))
# C = 5 * (F-32) / 9
# print("{}º Farenheit é igual a {:.2f}º Celsius!".format(F, C))

#EXE 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

# print("Vamos converter graus Celsius, em Farenheit")
# C = int(input("Qual a temperatura em Celsius? "))
# F = C * (9 / 5) + 32
# print("{}º Celsius é igual a {:.2f}º Farenheit!".format(C, F))

#EXE 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
            # A - o produto do dobro do primeiro com metade do segundo .
            # B - a soma do triplo do primeiro com o terceiro.
            # C - o terceiro elevado ao cubo.

# print("Vamos realizar o calculo do Exercício 11")
# nu1 = int(input("Digite x (inteiro): "))
# nu2 = int(input("Digite y (inteiro): "))
# nu3 = float(input("Digite z (real): "))
# A = (nu1 * 2) + (nu2 / 2)
# B = (nu1 * 3) + nu3
# C = nu3 ** 3
# print("O valor de A é {}\nO valor de B é {:.2f}\nO valor de C é {:.2f}".format(A, B, C))

#EXE 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#         usando a seguinte fórmula: (72.7*altura) - 58

# print("Medidor de peso Ideal")
# weight = float(input("Digite a sua altura em metros: "))
# ideal = (72.7 * weight) - 58
# print("Seu peso ideal é {:.2f} kilos".format(ideal))

#EXE 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#         utilizando as seguintes fórmulas:
#         Para homens: (72.7*h) - 58
#         Para mulheres: (62.1*h) - 44.7

# print("Medidor de peso Ideal Unissex")
# h = float(input("Digite sua altura em metros: "))
# s = int(input("Digite 1 caso seja Homem ou 2 se for Mulher: "))
# if s == 1:
#     ih = (72.7 * h) - 58
#     print("Seu peso ideal é {:.2f} quilos".format(ih))
# elif s == 2:
#     im = (62.1 * h) - 44.7
#     print("Seu peso ideal é {:.2f} quilos".format(im))
# elif s < 1 or s > 2:
#     print("Digite 1 ou 2 para esse campo.")

#EXE 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#         Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
#         São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça
#         um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável
#         excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#         Imprima os dados do programa com as mensagens adequadas.

# print("Iniciando CalculaPeixe")
# peso = float(input("Digite o peso de peixes de hoje em quilos: "))
# excesso = peso - 50
# multa = excesso * 4
# if peso > 50:
#     print("João,sua pesca de hoje passou {:.2f} quilos do limite estipulado. O que gerou uma multa de {:.2f} reais!".format(excesso, multa))
# else:
#     print("João,sua pesca de hoje não gerou nenhuma multa!")

#EXE 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário
#          no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#          faça um programa que nos dê:
                # salário bruto.
                # quanto pagou ao INSS.
                # quanto pagou ao sindicato.
                # o salário líquido.
                # calcule os descontos e o salário líquido, conforme a tabela abaixo:

# print("Vamos calcular o seu Salário")
# money_hour = float(input("Digite o quanto voce ganha por hora em reais: "))
# work_hour = float(input("Digite quantas horas foram trabalhadas esse mês: "))
# gross_salary = money_hour * work_hour
# ir = gross_salary * 0.11
# inss = gross_salary * 0.08
# sindicato = gross_salary * 0.05
# total_descontos = ir + inss + sindicato
# net_salary = gross_salary - total_descontos
# print("Vamos aos valores:\nSalário Bruto: {:.2f} reais\nContribuição ao INSS: {:.2f} reais\nContribuição ao Sindicato: {:.2f} reais\nSalário Liquido: {:.2f} reais".format(gross_salary,inss,sindicato,net_salary))

#EXE 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#         Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#         que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# print("Iniciando o TintaCerta")
# size = float(input("Quantos metros quadrados tem a área a ser pintada? "))
# cust_area = size / 3
# tin_liters = 18
# tin_price = 80
# tin_amount = cust_area / tin_liters
# tin_amount_int = round(tin_amount + 0.5)
# total_price = tin_amount_int * tin_price
# if tin_amount_int == 1:
#     print("É preciso de {} lata de tinta para pintar essa área!\nCusto total de {:.2f} reais.".format(tin_amount_int,total_price))
# else:
#     print("É preciso de {} latas de tintas para pintar essa área!\nCusto total de {:.2f} reais.".format(tin_amount_int,total_price))

#EXE 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#         Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00  #         ou em galões de 3,6 litros, que custam R$ 25,00.
#         Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#          - comprar apenas latas de 18 litros;
#          - comprar apenas galões de 3,6 litros;
#          - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é
#            considere latas cheias.






