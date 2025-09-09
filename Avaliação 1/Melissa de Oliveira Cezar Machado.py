# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 0/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

def categoria_imc(imc):
    if imc <= 18.5:
        return "Abaixo do peso."
    elif imc <= 24.9:
        return  "Peso normal."
    elif imc <= 29.9:
        return "Sobrepeso."
    elif imc <= 34.9:
        return "Obesidade Grau 1"
    elif imc <= 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

peso = float(input("digite seu peso: "))
altura= float(input("digite sua altura: "))

imc =  peso / (altura * altura)

categoria = categoria_imc(imc)

print (f"Seu imc é: {imc}\nSua categoria é: {categoria}")


 

