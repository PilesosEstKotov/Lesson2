""" Модуль 3 """

PushkinAge = input("Введите год рождения А.С.Пушкина:\n")
PushkinTrueAge = 1799
PushkinTrueBornday = "6 июня"
if int(PushkinAge) == PushkinTrueAge:
    PushkinBornday = input("Верно. а какой день рождения?\n")
    if PushkinBornday == PushkinTrueBornday:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверно")