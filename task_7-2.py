"""Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их 
придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных
букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они
разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух передаст вам автоматически в переменную text_person в 
виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и
Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести:
"Количество фраз должно быть больше одной!".

Пример:
На входе:
text_peson = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе:
Парам-пам-пам
"""

# text_person = """СОНЦА неба сагравае цяплынёй,
#  И сланечник залатицца над зямлей"""
text_person = "пара-ра-рам рам-пам-папам па-ра-па-дам"


def get_list_phrases(text: str):
    return text.lower().replace("-", "").split()


def checking_rhyme(array_phrases, set_letter):
    count_syllable_in_first_phrases = 0
    for char in array_phrases[0]:  # определяем количество слогов в первом слове
        if char in set_letter:     # и берем это за эталон
            count_syllable_in_first_phrases += 1
    for i in range(1, len(array_phrases)): # сравниваем количество слогов в 
        syllable_current_phrase = 0       # следующих словах с эталоном
        for item in array_phrases[i]:
            if item in set_letter:
                syllable_current_phrase += 1
        if syllable_current_phrase != count_syllable_in_first_phrases:
            return False 
    return True


if len(get_list_phrases(text_person)) == 1:
    print("Количество фраз должно быть больше одной!.")
    exit()

set_letter = {"а", "о", "у", "и", "е", "ы", "я", "э", "ю", "ё"}

(
    print("Парам пам-пам")
    if checking_rhyme(get_list_phrases(text_person), set_letter)
    else print("Пам парам")
)
