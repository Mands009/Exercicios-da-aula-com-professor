# Calculadora se é melhor usar alcool ou gasolina
Alcool = float(input("Digite o valor do alcool: "))
Gasolina = float(input("Digite o valor da gasolina: "))
Calculadora = Alcool/Gasolina
 
print ("-" * 35)
print("Resultado: ", Calculadora)
if Calculadora <=0.70:
    print("Devo usar alcool!")
else:
    print("Devo usar gasolina!")