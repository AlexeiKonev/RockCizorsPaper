import  random

# создаем массив вариантов
variants = ['бумага','ножницы','камень']
#пользователь выбирает
user_choise = input('выберите свой вариант введите \n0 для выбора бумаги\n1 для выбора ножниц\n2 для выбора камень\n')
#выбранный вариант переводим в целочисленное из строчного
user_choise_number = int(user_choise)
# генерируем случайный выбор
choisen_variant = random.choice(variants)
user_choise_variant = variants[user_choise_number]
#выводим выбраный вариант
print(' ты выбрал  '+ ' '+ user_choise_variant)
#выводим выбраный вариант
print(' комп выбрал  '+ ' '+ choisen_variant)
#задаем условия победы
win_user = False
win_pc = False

if  variants[user_choise_number] == choisen_variant:
    print('ничья')
#если у игрока бумага а компа ножницы то прсваевыем победу компу
elif variants[user_choise_number] ==  variants[0] and choisen_variant == variants[1]:
    win_pc = True
    win_user = False
    print('комп выйграл')
#если у игрока бумага а компа камень то прсваевыем победу игроку
elif variants[user_choise_number] ==  variants[0] and choisen_variant == variants[2]:
    win_pc = False
    win_user = True
    print('ты выйграл')
#если у игрока ножницы, а у компа бумага то присваевыем победу игроку
elif variants[user_choise_number] ==  variants[1] and choisen_variant == variants[0]:
    win_pc = False
    win_user = True
    print('ты выйграл')
#если у игрока ножницы, а у компа камень то присваевыем победу компу
elif variants[user_choise_number] ==  variants[1] and choisen_variant == variants[2]:
    win_pc = True
    win_user = False
    print('комп выйграл')
#если у игрока камень, а у компа ножницы то присваевыем победу игроку
elif variants[user_choise_number] ==  variants[2] and choisen_variant == variants[1]:
    win_pc = False
    win_user = True
    print('ты выйграл')
#если у игрока камень, а у компа бумага то присваевыем победу игроку
elif variants[user_choise_number] ==  variants[2] and choisen_variant == variants[0]:
    win_pc = True
    win_user = False
    print('комп выйграл')