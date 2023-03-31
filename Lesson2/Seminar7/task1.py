# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе 
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
vowels = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", "й", "ё" ]
poem = input("Введите фразы:").split()
if len(poem) < 2:
    print("Введите больше одной фразы")
else:
    countVowels = []
    for i in poem:
        countVowels.append(len([x for x in i if x.lower() in vowels]))
    
    if set(countVowels) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")