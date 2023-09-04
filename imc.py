print("Ola, eu sou a samy, e irei calcular seu índice de massa corporal")
print("\n")
print("IMPORTANTE..... coloque ''.'' para para separar kilos de gramas e metros de centimetros, em vez de '',''")
print("EXEMPLO peso 50.59    Altura 1.70")
print("\n")
peso = float(input('Informe o seu peso:\n '))
altura = float(input('Informe sua altura:\n '))
imc = peso / (pow(altura, 2))

print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print("ATENÇÃO !! Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso ideal(parabens)")
elif 25 <= imc < 29.9:
    print("Levemente acima do peso")
elif 30 <= imc < 34.9:
    print("ATENÇÃO !! Obesidade Grau I")
elif 35 <= imc < 39.9:
    print("ATENÇÃO!! Obesidade Grau II")
else:
    print("ATENÇÃO !!!Obesidade Grau III ou Mórbida")