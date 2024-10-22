# Пратическая 2
"""#Задание 1

def f(n1,k):
  d=0
  for i in range(1,k,1):
     d=n1/100*10
     n1=n1+d
  return(n1)

n1=float(input("Введите растоянию в первый день "))
k=int(input("k-й день"))
n1=f(n1,k)

print(f"Дистанция на {k}-й день: {n1} км")

"""
"""#Задание 2


def число(n):
 binary_number=""

 while n > 0:
  binary_number = str(n % 2) + binary_number
  n = n // 2
 return binary_number

n=int(input("Введите число "))
bin=число(n)
print(f"Двоичное представление числа равно {bin}")    
"""
"""#задание 4
y=2021
k=620000
k1=1500000
while k<k1:
   k2=k/100*3.7
   k=k+k2
   y=y+1
print(y) """
"""#Задание 5
n=int(input("Введите число "))
s=[]
for i in range(1,n):
   if n%i==0:
      if i%2==1:
       s.append(i)
s1=0
for i in s:
   s1=s1+i
print(s1)
"""
"""#задание 6

n1=int(input("Введите количество делителей n: "))
def делитель(n):
  s=[]
  for i in range(1,n+1):
     if n%i==0:
         s.append(i)
  return(len(s))
print(f"C делитеями {n1}")
for i in range(0,200+1):
   ss=делитель(i)
   if ss==n1:
      print(i, end=" ")
 """
"""#задание 3

def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n =n // divisor
        divisor += 1
    
    return factors

# Пример использования
number = int(input())
factors = prime_factors(number)
print(f"Простые множители числа {number}: {factors}")"""
"""#Задание инд 1

def cal(price_per_kg):
    costs = []
    for kg in range(12, 21, 2):  # Используем целые числа для удобства, затем преобразуем в вещественные
        kg = kg / 10  # Преобразуем в вещественное число
        cost = price_per_kg * kg
        costs.append((kg, cost))
        
    return costs

prickg = float(input("Введите стоимость 1 кг конфет: "))

costs = cal(prickg)

print("Стоимость конфет:")
for kg, cost in costs:
    print(f"{kg} кг: {cost:.2f} руб.")"""
"""#Задание инд 2

import math

x = int(input("Введите значение x: "))
smath = math.sin(x)
print(f"Значение из math.sin: {smath}")

epsilon = float(input("Введите погрешность"))
a = x   
n = 1
s = 0  

while abs(a) > epsilon:
    s += a
    a = (-1)**n * x**(2*n-1) / math.factorial(2*n-1)
    n += 1
print(f"sin({x}) = {s} (число итераций: {n-1})")"""
"""#Задание инд 3
T=500
s=0
t=[20,40,50,60,10,20]
for i in t:
   s=s+i
print(f"Мастер потратить {s}")
print(f"Мастер обслужить {len(t)}")
"""
# Практическая 3
"""#Задание 1

from random import randint 

a = [randint(-10, 10) for i in range (20)]
print(a)
a_pow=[]

for i in range(0,len(a)):
    a.append(i**2)
    a_pow.append(a[i]**2)
print("Квадрат чисел")
print(a_pow)"""
"""#Задание 2


from random import randint 

a = [randint(-10, 10) for i in range(20)]
 
print (a)
d1=[]
d=[]
for i in a:
    if a.count(i)>1:
        if i not in d:
            d.append(i)
    else:
        if i not in d1:
            d1.append(i)
print("Встреяаются более 1 раза ",d)

print("Встречаюся 1 раз",d1)"""
"""#Задание 3
from random import randint 

a = [randint(-10, 10) for i in range(20)]
b=[randint(-10,10) for i in range(20)]
print(a)
print(b)
s=[]
for i in b:
    if a.count(i)==0:
        s.append(i)
print(s)
"""
"""#Задание 4
from random import randint 

a = [randint(-10, 21) for i in range(20)]
print(a)
for i in range(len(a)):
    if a[i]==20:
        a.pop(i)
        a.insert(i,200)
print(a)"""
"""#Задание 5
from random import randint
a=[randint(0,17) for i in range(20)]

print(a)
print("Четные число в списке до встречи 15 ")
for i in a:
   if i==15:
      break
   elif (i%2==0):
      print(i,end=" ")"""
"""#Задание 1инд

kart = ["Черви", "Бубны", "Крести", "Пики"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

deck = []

for i in kart:
    for j in ranks:
        card = f"{i} {j}"
        deck.append(card)


from random import randint

def ran(n):
   l=[]
   for i in range(n):
      s=deck[randint(0,len(deck)-1)]
      l.append(s)
      deck.remove(s)
      s=0
   return l

k=int(input("Введите количество игроков "))
p=int(input("Введите количество раздаваемых карт "))
k2=int(input("Введите количесво колоды карт"))
while ((k2<k*p) or (k2 >52) ):
    print("Неправилььный ввод ")
    k=int(input("Введите количество игроков "))
    p=int(input("Введите количество раздаваемых карт "))
    k2=int(input("Введите количесво колоды карт"))
    
deck=deck[:k2:1]
print(deck)
ki=[]

for i in range(k):
    ki.append(ran(p))

print("Карты игроков")
n=1
for i in ki:
    print(f"Колоды {n}-ого игрока")
    n=n+1
    print(i)

print("Оставшие колоды карты")
print(deck)"""

#Практическаы 4
"""#Задание 1
file=open("date.txt","w",encoding="utf-8" )

fd=True
while fd==True:
    d=input("Вводите строку ")
    file.write(d+"\n")
    if d==".":
        fd=False
        print("Файл записан")

file.close()

"""
"""#Задание 2
name=input("Введите имя файла")
with open(name,"r" ,encoding="utf-8") as file:
    sd=file.readlines()

with open(name,"w",encoding="utf-8" ) as file:
    s=1
    for i in sd:
        file.write(f"{s} {i}")
        s+=1"""
"""#Задание 3 разработать приложение для разделение файла на части приложение принимает на вход имя файла для разделение и целое число
#  n на выходе у приложение  множество файлоов каждый из которых содержит не более чем N строк из исходного файла 
f=input()
N=int(input("Введите N "))
with open(f,"r",encoding="utf-8") as file:
    d=file.readlines()


part=[]                 
n=1
for i in range(0,len(d),N):
    part=d[i:i+N]
    print(part)

    with open(f"{n}.txt", 'w', encoding='utf-8') as part_file:
            part_file.writelines(part)
    n=1+n
"""
"""#задание 4
 
d=input()
s=input()
d1=input("Имя выходного файла ")
with open(d,"r",encoding="utf-8") as file:
    f=file.read()
with open(s,"r",encoding="utf-8") as file:
    f1=file.read()

with open(f"{d1}.txt","a",encoding="utf-8") as file:
    file.write(f)
    file.write(f1)"""
"""#доп1 Разработать приложение которыые выводиьт N Первых строк 
d=input()
N=int(input())
with open(d,"r") as file:
    for i in range(N):
        s=file.readline()
        print(s , end="")

"""
"""#доп2 Разработать приложение которыые выводиьт N последных строк 
d=input("Введите имя файла")
s=True
N=int(input("Введите N "))

with open(d,"r") as file:
    d1=file.readlines()            
d1=d1[-N::]
print(f"{N} конечные строчки файла {d}")

for i in range(len(d1)):
    print(d1[i],end="")"""
"""#Доп задание 3 
string=input()
s=string.split(" ")"""
"""if len(s)==4:
    print(s)
    
else:
    print("Неправильный ввод ")"""
"""s.remove(' ')
print(s)""" 