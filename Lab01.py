from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

#zadanie 1

x=arange(56, 101, 1)
y = 2*x**2 + 2*x + 2
print(y)

#zadanie 2

print("Podaj liczbę ...")
x01=int(input())
for i in range(x01+1):
    if i==0:
        y01=1
    else:
        y01 = y01*i
print(y01)

#zadanie 3

print("Podaj rozmiar listy ...")
n=int(input())
lista=[]
for i in range(n):
    print("Podaj wartość")
    lista.append(int(input()))
k=lista[0]
for i in range(len(lista)):
    if k>lista[i]:
        k=lista[i]
print("Index : ", lista.index(k),"Wartość" , k)

#zadanie 4

print("Podaj długość dziedziny ...")
x04 = int(input())
x_values = zeros(x04)
y_values = zeros(x04)

for i in range(x04):
    x_values[i] = i
    y_values[i] = tan(x_values[i]**3-x_values[i]*42)

plot(x_values, y_values)
show()