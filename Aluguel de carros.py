dia = int(input("Quantidade de dias:"))
km = float(input("Quilometros rodados:"))

d = dia*60
k = km*0.15
soma= d+k
print("R${} por {} dias, {:.2f}KM por R${:.2f} \nTotal: R${}".format(d, dia, km, k, soma))