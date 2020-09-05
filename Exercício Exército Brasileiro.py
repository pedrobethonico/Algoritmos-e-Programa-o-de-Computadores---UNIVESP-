print ("Você está prestando o Processo Seletivo para entrar no Exército Brasileiro. Responda esse questionário e saiba se você foi aprovado!")
       
nome = input ("Escreva seu nome:")
idade = int(input ("Escreva sua idade:"))
peso = float (input ("Escreva seu peso:"))
altura = float (input ("Escreva sua altura:"))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print ("Parabéns",nome,"! Você foi aprovado no Processo Seletivo do Exército Brasileiro!")
else:
    print ("Você foi reprovado no Processo Seletivo do Exército Brasileiro! Tente denovo no próximo ano.")
    
       
