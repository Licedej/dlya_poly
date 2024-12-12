# № 1


def f(a):
  a0=a[0]
  a[0]=a[-1]
  a[-1]=a0
  return a
m = int(input('Введите длину массива: '))
a=[input() for i in range(m)]
print('Исходный массив:', a)
print('Полученный массив:', f(a))


# № 2

def f(x,y):
  a=x
  b=y
  while x!=0 and y!=0:
    if x > y:
      x=x%y
    else:
      y=y%x
  return str(a//(x+y))+'/'+str(b//(x+y))
a,b = map(int,input('Введите a и b: ').split())
d,c = map(int,input('Введите d и c: ').split())
print(f(a,b)) 
print(f(d,c))



# № 3

import random 
n = int(input('Введите размерность матрицы: '))
mat = [[random.randrange(10) for i in range(n)] for j in range(n)]
print(mat)


def prov(mat):
    first = sum(mat[0])
    for k in range(1, n):
        if sum(mat[0]) != first:
            return False
    for k in range(0, n):
        if sum([row[k] for row in mat]) != first:
            return False
    h, h_2 = 0, 0
    for k in range(0, n):
        h = h + mat[k][k]
    if h != first:
        return False
    for i in range(n):
        h_2 = h_2 + mat[n - 1 - i][i]
    if h_2 != first:
        return False
    return True
if prov(mat):
    print('Это магический квадрат')
else:
    print('Не магический квадрат')


# № 4

from random import randint
m1=[randint(-100, 100) for x in range(15)]
m2=[randint(-100, 100) for x in range(15)]
m3=[randint(-100, 100) for x in range(15)]
print('Массив:',m1,'Сумма элементов: ',sum(m1),'Среднеарифметическое: ',sum(m1)/len(m1))
print('Массив:',m2,'Сумма элементов: ',sum(m2),'Среднеарифметическое: ',sum(m2)/len(m2))
print('Массив:',m3,'Сумма элементов: ',sum(m3),'Среднеарифметическое: ',sum(m3)/len(m3))


# № 5

from random import randint
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(m):
    brr = list()
    for j in range(n):
        brr.append(randint(-10, 10))
    arr.append(brr)
print(arr)
summi = {}
for i in arr:
    summi.update({sum(i):i})
print(f'максимальная сумма {max(summi.keys())} у строчки {summi.get(max(summi.keys()))}')
print(f'минимальная сумма {min(summi.keys())} у строчки {summi.get(min(summi.keys()))}')


# № 6

from random import sample, randint
m, n = randint(2, 10), randint(2, 10)
arr = list()
for i in range(n):
    brr = sample(range(-30, 30), m)
    arr.append(brr)
print(arr)
for i in arr:
    if i[i.index(min(i))] % 2 == 0:
        i[i.index(min(i))] = 0
    else:
        i[i.index(min(i))] = 1
print(arr)