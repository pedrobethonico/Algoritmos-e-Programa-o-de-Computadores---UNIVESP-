#Calculo do IMC - Algoritmos e Programação de Computadores I - UNIVESP

#Entrada de Dados do Usuário

print("Olá, neste programa iremos calcular o seu Indice de Massa Corpórea - IMC e lhe informar em qual faixa de peso você se enquadra.")

nome = input ("Qual o seu nome?" )
peso = float(input("Qual o seu peso em Kg? "))
altura = float(input("Qual sua altura em metros? "))

#Calculo do IMC
imc = peso / (altura **2)
print ("O Indíce de Massa Corpórea de", nome,"é", imc)

#Entruturas de condição
if imc < 18.5:
      print (nome, "está ABAIXO do peso normal!")
elif imc >= 18.5 and imc < 25:
    print (nome, "está com o PESO NORMAL!")
elif imc >= 25 and imc < 30:
    print (nome, "está com SOBREPESO!")
else:
    print (nome, "está OBESO!")
    
