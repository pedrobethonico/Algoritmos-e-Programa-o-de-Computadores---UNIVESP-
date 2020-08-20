#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DESAFIO SONECA
# Equação de 2° Grau

#Considere a equação com seguinte formato: ax2 + bx + c = 0


#Inserção das variáveis
a = float(input ("Escreva a variável a: "))
b = float(input ("Escreva a variável b: "))
c = float(input ("Escreva a variável c: "))

print ("A equação de 2° Grau à ser resolvida é",a,"x2 +",b,"x2 +",c,"= 0")

#DELTA
delta = b**2-4*a*c
print ("O valor de delta é", delta) 

raizdelta = delta ** 0.5
print ("A raiz de delta é", raizdelta)

#RAÍZES
x1 = (-b + raizdelta)/(2*a)
x2 = (-b - raizdelta)/(2*a)

print ("O valor de x1 é",x1)
print ("O valor de x2 é",x2)


# In[ ]:




