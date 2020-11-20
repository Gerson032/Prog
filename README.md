# Progdia = int(input("Quantidade de dias:"))
km = float(input("Quilometros rodados:"))

d = dia*60
k = km*0.15
soma= d+k
print("R${} por {} dias, {:.2f}KM por R${:.2f} \nTotal: R${}".format(d, dia, km, k, soma))
c = float(input("Digite a temperatura em graus Celsius:"))
f = ((9*c)/5)+32
print("{}C sao {}F".format(c, f))

real = float(input("Digite o valor em Real a ser convertido: "))
dolar = 5.37*real
print("U${} equivale a R${}".format(real, dolar))
n = int(input("Digite um numero:"))
dobro = n*2
triplo = n*3
raizQ= n**(1/2)
print("O dobro de {} e:{}\nO triplo de {} e:{}\nA raiz de {} e:{}".format(n, dobro, n, triplo, n, raizQ))

n = float(input("Nota:"))
n2 = float(input("Nota:"))

soma = (n+n2)/2
print("A media de {:.1f} e {:.1f} e: {:.1f}".format(n, n2, soma))

medida = float(input("Digite a medida em Quilometros: "))
metros = medida*1000
cm = medida*10000
mm = medida*100000
print("{:.0f} Quilometros Equivale a {:.0f} metros, {:.0f}centimetros, e {:.0f} milimetros".format(medida, metros, cm, mm))
from random import randint
from math import sqrt, hypot
num = randint(1, 10)
num2 = randint(1, 10)
print("CatetoA: {}, CatetoO: {}, Hipotenusa: {:.2f}".format(num, num2, hypot((num),(num2))))
import random
alunos = ("joao", "maria", "clara", "matheus")
print("O aluno escolhido e: {}".format(random.choice(alunos)))
n = int(input("Digite um numero para gerar a tabuada: "))
print("_"*15)
print("{} x {:2} = {}".format(n, 1, n*1))
print("{} x {:2} = {}".format(n, 2, n*2))
print("{} x {:2} = {}".format(n, 3, n*3))
print("{} x {:2} = {}".format(n, 4, n*4))
print("{} x {:2} = {}".format(n, 5, n*5))
print("{} x {:2} = {}".format(n, 6, n*6))
print("{} x {:2} = {}".format(n, 7, n*7))
print("{} x {:2} = {}".format(n, 8, n*8))
print("{} x {:2} = {}".format(n, 9, n*9))
print("{} x {:2} = {}".format(n, 10, n*10))
print("_"*15)
import math
n = int(input("Digite o numero:"))
raiz = math.sqrt(n)
print("A raiz de {} e: {:.3f}".format(n, raiz))
