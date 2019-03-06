from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

#zadanie 1

#x=linspace(56, 100, 45)
#y = 2*x**2 + 2*x + 2
#print(y)

#zadanie 2

#print("Podaj liczbę ...")
#x01=int(input())
#for i in range(x01+1):
    #if i==0:
        #y01=1
    #else:
        #y01 = y01*i
#print(y01)

#zadanie 3

#lista=[9, 0, 5, 7, 2]
#k=lista[0]
#for i in range(len(lista)):
    #if k>lista[i]:
        #k=lista[i]

#print(lista.index(k), k)

#zadanie 4

x04 = int(input())
x_values = zeros(x04+1)
y_values = zeros(x04+1)

for i in range(x04+1):
    x_values[i] = i
    y_values[i] = tan(x_values[i]**3-x_values[i]*42)

plot(x_values, y_values)
show()