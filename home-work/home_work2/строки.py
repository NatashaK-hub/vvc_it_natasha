def level_1():
    print ("Введите текст:")
    text=str(input())
    print("Введите цифру, соответствующую желаемому методу")
    print("1 - upper(); 2 - lower(); 3 - capitalize()")
    metod=int(input())
    if metod==1: print("Ваша строка:", a, "   Ваш метод: upper()", "  Результат:", text.upper())
    if metod==2: print("Ваша строка:", a, "   Ваш метод: lower()", "  Результат:", text.lower())
    if metod==3: print("Ваша строка:", a, "   Ваш метод: capitalize()", "  Результат:", text.capitalize())

def level_2():
    print("Введите текст:")
    text = str(input())
    print("Введите слово, содержащееся в этом тексте (в той же форме):")
    word=str(input())
    print ("Позиция первого вхождения слова", word, "в строке:", text.find(word))
    print ("Введите, на что будем менять слово: ", word)
    change=str(input())
    print ("Результат замены:", text.replace(word, change))
    print ("Введите букву, а мы посчитаем, сколько раз она встречается в начальной фразе")
    letter=str(input())
    print ("Буква", letter, "встречается во фразе", text.count(letter))

def level_3():
    print("Введите строку:")
    text=str(input())
    print ("Введите символ, по которому строку нужно разделить:")
    symbol_1=str(input())
    print("Введите символ, по которому строку нужно собрать:")
    symbol_2 = str(input())
    splitted_text=text.split(symbol_1)
    sentence=symbol_2.join(splitted_text)
    print ("Результат:", sentence)

def level_4():
    print ("Введите три строки ЧЕРЕЗ ЗАПЯТУЮ (без пробелов)")
    text_4a, text_4b, text_4c=input().split(',')
    print ("Является ли первая строка числом?")
    print(text_4a.isdigit())
    print ("Является ли вторая и третья строка буквами?")
    print (text_4b.isalpha())
    print("Третья строка без пробелов:", text_4c.strip())

def level_5():
    print ("Введите текст:")
    text=input()
    text_1=text.split(';')
    text_2=' '.join(text_1)
    text_3=text_2.replace("somE !", "somE!")
    text_3=text_3.strip()
    text_3=text_3.capitalize()
    print (text_3)

print ("Введите уровень игры (число от 1 до 5)")
level=int(input())
if level==1:
    level_1()
if level==2:
    level_2()
if level==3:
    level_3()
if level==4:
    level_4()
if level==5:
    level_5()

