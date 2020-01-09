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

# print("Vamos realizar o calculo do Exercico 11")
# nu1 = int(input("Digite x (inteiro): "))
# nu2 = int(input("Digite y (inteiro): "))
# nu3 = float(input("Digite z (real): "))
# A = (nu1 * 2) + (nu2 / 2)
# B = (nu1 * 3) + nu3
# C = nu3 ** 3
# print("O valor de A é {}\nO valor de B é {:.2f}\nO valor de C é {:.2f}".format(A, B, C))

#EXE 12 -