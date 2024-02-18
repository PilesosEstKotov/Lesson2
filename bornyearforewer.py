""" Модуль 4 """

PushkinAge = input("Введите год рождения А.С.Пушкина:\n")
PushkinTrueAge = 1799
while int(PushkinAge) != PushkinTrueAge:
    print("неверно")
    PushkinAge = input("Введите год рождения А.С.Пушкина:\n")
else:
    print("Верно")