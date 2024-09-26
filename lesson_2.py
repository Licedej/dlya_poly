dele = input('Введите 2 числа \n')

def prov(nom):
    try:
        nom1, nom2 = map(float, nom.split())
        return True
    except ValueError:
        return False

if len(dele.split()) == 2:
    if prov(dele):
        a, b = map(str, dele.split())
        if b != "0":
            print(f'{a}/{b} = {float(a)/float(b)}')
        else:
            print('На ноль делить нельзя!')
    else: print('Введите 2 ЧИСЛА')
else: print('Введите только 2 числа')


cost = input('Введите стоимость покупки. \n')
    
def prov2(nom):
    try:
        float(nom)
        return True
    except ValueError:
        return False

if prov2(cost): 
    if float(cost) > 20:
        sk = round(float(cost)*0.35, 2)
        it = round(float(cost) - sk, 2)
        print(f'Итоговая стоимость покупки: {it}. Вы экономите {sk}.')
    else: 
        print(f'Скидка в 35% распространяется на покупки стоимость, которых превышает 20 у.е. Вам до скидки не хватает: 20 - {cost} = {20 - float(cost)}.')
else: print('Использованы недопустимые символы')

m = input('Введите целое число [1; 12] \n')
    
def prov3(st):
    try:
        st.isdigit() == True
        if (0 < int(st) < 13) == True:
            return True
        elif ValueError:
            return False
    except ValueError:
        return False

month = {'1':'январь, зима', '2':'февраль, зима', '3':'март, весна', '4':'апрель, весна', '5':'май, весна',\
          '6':'июнь, лето', '7':'июль, лето', '8':'август, лето', '9':'сентябрь, осень', '10':'октябрь, осень',\
          '11':'ноябрь, осень', '12':'декабрь, зима'}

if prov3(m):
    print(month[m])
else: print('Введите одно число от 1 до 12!')