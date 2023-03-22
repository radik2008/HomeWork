# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# *Пример:*
# ноутбук
#     12
text = str(input("Введите слово:"))
text.lower()
print(text)
count=0
for index in text:
    if index == 'a' or index == 'e' or index == 'i' or index == 'o' or index == 'u' or index == 'l' or index == 'n' or index == 's' or index == 't' or index == 'r':
        count+=1
    if index == 'd' or index == 'g':
        count += 2
    if index == 'b' or index == 'c' or index == 'm' or index == 'p':
        count += 3
    if index == 'f' or index == 'h' or index == 'v' or index == 'w' or index == 'y':
        count += 4
    if index == 'k':
        count += 5
    if index == 'j' or index == 'x':
        count += 8
    if index == 'q' or index == 'z':
        count += 10

print(f"Количество очков равно {count}")