peso = float(input("Digite o peso (kg):"))
altura = float(input("Digite a altura (m):"))

imc = peso/ (altura ** 2)

print("IMC =", round(imc, 2))

if imc > 25:
    print("acima do peso")
else:
    print("peso normal")
    