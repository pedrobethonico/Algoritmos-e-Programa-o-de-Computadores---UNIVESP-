#Iniciar dando uma introdução com o nome da Loja. Aprendi esse comando na internet e é util para dar enfase em algumas palavras. 

#ETAPA 1: Apresentação do programa para o usuário. 

print('{:=^40}'.format(' BETHÔNICO STORE '))

print('Esse programa foi criado para que você, funcionário da Bethônico Store, possa calcular os descontos dados aos clientes de maneira padronizada entre todos os funcionários e assim gerar previsibilidade para o setor  de Planejamento de Vendas e Operações (SALES AND OPERATIONS PLANINING - S&OP)')

#ETAPA 2: Entrada com os dados de pagamento por parte do funcionário da Bethônico Store.  

preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual é a opção? '))


#ETAPA 3: Estruturas de condição para determinação do preço final do produto de acordo com número de parcelas. 
if forma == 1:
    total = preço - (preço*10/100)
elif forma == 2:
    total = preço - (preço*5/100)
elif forma == 3:
    total = preço
    parcela = total/2
    print("Sua compra será parcelada em 2x de R$", parcela)
elif forma == 4:
    total = preço + (preço * 20 / 100)
    totparcela = int(input("Quantas parcelas? "))
    parcela = total / totparcela
    print("Sua compra será parcelada em", totparcela, "x de", parcela)

print ("Sua compra no valor de R$", preço, "terá um preço total de R$", total, "no final")
