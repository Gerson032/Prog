medida = float(input("Digite a medida em Quilometros: "))
metros = medida*1000
cm = medida*10000
mm = medida*100000
print("{:.0f} Quilometros Equivale a {:.0f} metros, {:.0f}centimetros, e {:.0f} milimetros".format(medida, metros, cm, mm))