# Выбираем факультет
import sys

print("1 - Красный        2 - Зеленый")
print("3 - Синий          4 - Желтый")
f = ""
a = input("Введи свой любимый цвет: ")
if (a == '1'):
    f = "Гриффиндор"
elif (a == '2'):
    f = "Слизерин"
elif (a == '3'):
    f = "Когтевран"
elif (a == '4'):
    f = "Пуффендуй"
else:
    print("Ты ввёл неправильное число!!!")
    sys.exit()
print()

# Выбираем патронус
print("1 - Математика     2 - Физкультура")
print("3 - Труд           4 - Информатика")
pat = ""
b = input("Введи свой любимый предмет в школе: ")
if (b == '1'):
    pat = "Олень"
elif (b == '2'):
    pat = "Заяц"
elif (b == '3'):
    pat = "Муравей"
elif (b == '4'):
    pat = "Собака"
else:
    print("Ты ввёл неправильное число!!!")
    sys.exit()
print()

#Выбираем палочку
print("1 - Единорог   2 - Дракон   3 - Феникс")
pal = ""
b = input("Какое твоё любимое магичиское существо: ")
if (b == '1'):
    pal = "14 дюймов, ива, волос единорога"
elif (b == '2'):
    pal = "10 дюймов, из древисины виноградной лозы, сердечная жила Дракона"
elif (b == '3'):
    pal = " 11 дюймов, остролист, перо феникса"
else:
    print("Ты ввёл неправильное число!!!")
    sys.exit()
print()

print()
print("------------------------------------------------------------------------------------")
print("Твой факультет - " + f)
print("Твой патронус - " + pat)
print("Твоя палочка - " + pal)
print("------------------------------------------------------------------------------------")