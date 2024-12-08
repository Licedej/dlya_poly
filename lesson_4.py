# № 1

k, i = 0, 0
n, m, l = [], [], []
a = input()
b = a + 'н'
while i < len(b):
    l.append(b.index('н', i,))
    i += 1
l = set(l)
for i in l:
    m.append(i)
for i in range(len(m) - 1):
    if m[i + 1] == m[i] + 1:
        k += 1
    else:
        n.append(k + 1)
        k = 0
print(a.replace('н', '!'))
print(max(n))


# № 2

def func(text, b=0, i=0):
    if text[i] == '(':
        b = i + 1
    elif text[i] == ')':
        return slice(b, i)
    return func(text, b, i + 1)
 
text = input()
print(text[func(text)])


# № 3

str = input()
 
for w in str.split(): 
    if(w.startswith("а") and w.endswith("я")): 
        print(w) 