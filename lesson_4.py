# № 1

k, i = 0, 0
n, l = [], []
a = input()
b = a + '+н'
while i < len(b):
    l.append(b.index('н', i,))
    i += 1
l = list(set(l))
for i in range(len(l) - 1):
    if l[i + 1] == l[i] + 1:
        k += 1
    else:
        n.append(k + 1)
        k = 0
print(a.replace('н', '!'))
print(max(n))


# № 2

def func(text):
    if '(' and ')' in text:
        i = text.index('(')
        while text[i] != text[text.index(')')]:
            i += 1
        return slice(text.index('(')+1, i)
text = input()
print(text[func(text)])


# № 3

str = input()
for w in str.split(): 
    if(w.startswith("а") and w.endswith("я")): 
        print(w) 