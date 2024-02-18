""" Модуль 5 """

PushkinAge = input("Введите год рождения А.С.Пушкина:\n")
PushkinTrueAge = 1799
PushkinTrueBornday = "6 июня"
while int(PushkinAge) != PushkinTrueAge:
    PushkinAge = input("Неверно, введите правильный год рождения А.С.Пушкина:\n")
else:
    print("Верно")
    PushkinBornday = input("теперь назовите дату рождения А.С.Пушкина:\n")
    while PushkinBornday != PushkinTrueBornday:
        PushkinBornday = input("Неверно, назовите правильную дату рождения А.С.Пушкина:\n")
    else:
        print("Верно")
