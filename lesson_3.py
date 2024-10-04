a = int(input())
l = 0
for i in range(1, a+1):
    l += i*i
print(l)


n = 9
for i in range(1,n+1):
    print(*("{:3}".format(i*j) for j in range(1, n+1)))