import re

# № 1

text = input()
if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text):
    print('private')
elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', text):
    print('taxi')
else:
    print('Не не то, что-то, но не то, не то...')


# № 2

text = input()
print(len(re.findall(r'\b\w[\w-]*\b', text)))


# № 3

text = input()
for i in re.findall(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', text):
     text = text.replace(i, '(TBD)')
print(text)
ext = input()
print(re.findall(r'(?:[АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ]{2,}[ ]*)+', text))