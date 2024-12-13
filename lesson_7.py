# № 1
def read_last(lines, file):
    f = open(file, 'r', encoding='utf-8')
    stroki = f.readlines()
    if len(stroki) >= n and n > 0:
        for i in stroki[len(stroki) - lines:]:
            print(i)

n = int(input())
read_last(n, r'article.txt')


# № 2
import os 

dir = os.getcwd()

def print_docs(directory):
    use_files = os.walk(directory)
    for i in use_files:
        print(f'В папке {i[0]} лежат: \n папки {", ".join([papka for papka in i[1]])} \n и файлы {", ".join([file for file in i[2]])} \n')
print_docs(dir)


# № 3
def longest_words(file):
    f = open(file, 'r', encoding='utf-8')
    stroki = f.readlines()
    dlinnoe = set()
    for i in stroki:
        nya = i.split()
        dlinnoe.add(max(nya, key=len))
    if len(dlinnoe) > 0: return max(dlinnoe, key=len)

print(longest_words('article.txt'))


# № 4
def redactor():
    file = open(f'{input('введите название файла: ')}.txt', 'w+', encoding='utf-8')
    text = 'пишите содержимое файла'
    print(text)
    while text != '':
        text = input()
        file.write(f'{text} \n')
    file.close()
redactor()