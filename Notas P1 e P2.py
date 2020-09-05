#Status do Aluno (Aprovado ou Reprovado)
print ("Olá")
print ("Nos próximos passos iremos descobrir de se você está aprovado ou reprovado nas disciplinas. Para começar, insira seu nome completo e seu registro acadêmico. Em seguida digite a nota da Prova 1 e a nota da Prova 2. Insira também a disciplina ao qual está realizando a consulta. ")
print ("Espero que tenha experiêcia!")

#Identificando o aluno
nome = input("Insira seu nome completo, por favor:")
ra = input("Agora, insira seu registro acadêmico:")
print ("Olá ", nome,". Seu Registro Acadêmico é: ", ra,". Para prosseguir insira nos próximos passos a sua nota da Prova 1 e da Prova 2. Ao fim, veja se esta aprovado ou reprovado.")

#Verificando >>>SE<<< o aluno está aprovado ou reprovado 
notap1 = input("Insira a nota da Prova 1 por favor: ")
notap2 = input("Agora, insira sua nota na Prova 2: ")
              
p1 = eval(notap1)
p2 = eval(notap2)
              
notafinal = ((0.4*p1)+(0.6*p2))
if notafinal >= 5:
    print ("Parabéns ",nome,"! Você está aprovado. Sua média é ",notafinal)
else:
    print ("Você está reprovado ", nome,"!!! Sua média final é", notafinal)
