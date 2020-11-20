from random import randint
from math import sqrt, hypot
num = randint(1, 10)
num2 = randint(1, 10)
print("CatetoA: {}, CatetoO: {}, Hipotenusa: {:.2f}".format(num, num2, hypot((num),(num2))))