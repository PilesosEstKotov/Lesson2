""" Модуль 6"""
# тест на то насколько ты хорошая фанатка BTS
def start_quiz():
    # участники группы BTS и их год рождения
    bts_members = {
        'RM': 1994,
        'Jin': 1992,
        'SUGA': 1993,
        'j-hope': 1994,
        'Jimin': 1995,
        'V': 1995,
        'Jungkook': 1997,
        'Иисус Христос': 0
    }

    correct_answers = 0
    wrong_answers = 0

    for member, birth_year in bts_members.items():
        user_answer = int(input(f"Введите год рождения {member} из BTS: "))
        if user_answer == birth_year:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Неправильно!")
            wrong_answers += 1

    total_questions = len(bts_members)
    percent_correct = correct_answers * 100 / total_questions
    percent_wrong = wrong_answers * 100 / total_questions

    print(f"\nКоличество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {wrong_answers}")
    print(f"Процент правильных ответов: {percent_correct}%")
    print(f"Процент неправильных ответов: {percent_wrong}%")


    repeat = input("\nХотите начать игру сначала? Да/Нет: ").lower()
    if repeat == 'да':
        start_quiz()
    else:
        print("Спасибо за игру!")

start_quiz()