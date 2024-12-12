# № 1 

a = int(input('Введите верхний предел сумму кубов натуральных чисел: '))
l = 0
for i in range(1, a+1):
    l += i**3
print(l)


# № 2 

n = 9
for i in range(1,n+1):
    print(*("{:^3}".format(i*j) for j in range(1, n+1)))

# № 2*

for i in range(9, 0, -1):
    lin = [i*j for j in range(1, 10)]
    for j in range(len(lin)):
        if len(str(lin[j])) == 1 and j != 8:
             print(f'{lin[j]}  ', end='')
        elif len(str(lin[j])) != 1 and j != 8:
             print(f'{lin[j]} ', end='')
        else:
             print(f'{lin[j]}', end='\n')