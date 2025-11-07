import random
print ("Введите длину лабиринта >=2")
n=int(input())
while n<2:
    print ("Кажется, вы ввели некорректный данные. Повторите ввод")
    n=int(input())
print ("Введите ширину лабиринта >2")
m=int(input())
while m<3:
    print ("Кажется, вы ввели некорректный данные. Повторите ввод")
    m=int(input())
health=10
things=[]###набор предметов
labirint=['key', 'exits', 'mnstr', 'trap', 'box']
otvet=0 ###условие выхода из лабиринта: комната exit, наличие ключа, желание покинуть лабиринт (otvet=1)

###заполнение комнат лабиринта:
for i in range (n*m-6):###рандомно заполняются оставшиеся комнаты
    rooms=['empty', 'mnstr', 'trap', 'box']
    random_room=random.choice(rooms)###random.choice возвращает случайный элемент списка
    labirint.append(random_room)
random.shuffle(labirint)###перемешивает список случайным образом 
labirint.insert (0, 'empty')###самая первая комната должна быть пустой

def empty():
    print ('Вы оказались в пустой комнате')

def box(health):
    print ("Вы нашли сундук. Получите рандомный бонус: ")
    bonus=['health+3', 'health+5', 'armor', "sword"]
    random_bonus=random.choice(bonus)
    print (random_bonus)
    if random_bonus=='health+3':
        print ("текущее здоровье:", health+3)
        return health+3
    if random_bonus=='health+5':
        print ("текущее здоровье:", health+5)
        return health +5
    if random_bonus=='armor':
        things.append('armor')
        print ("Ваш инвентарь:", things)
        return health
    if random_bonus=='sword':
        things.append('sword')
        print ("Ваш инвентарь:", things)
        return health
    

def key(things):
    print ('Поздравляю! Вы нашли ключ')
    things.append('key')
    print ("Ваш инвентарь:", things)
    return things

def exits(things):
    print ('Кажется, вы добрались до выхода из лабиринта')
    if 'key' in things:
        print ("Вы можете открыть портал ключом. ВВедите 1, если хотите покинуть лабиринт; и 0, если хотите остаться")
        otvet=int(input())
        if otvet==0:
            return 0
        else:
            return 1
    else:
        print ("Но вам нужно найти ключ")
        return 0
        
def monstr(things, health):
    print ("Вы попали в комнату к монстру")
    if ("sword" in things):
        print ("Атаковали его с помощью меча")
        return health
    elif ("armor" in things):
        print ("броня защитила вас от его когтей. Но больше у вас ее нет")
        things.remove("armor")
        return health
    else:
        print ("Вы оказались безоружны и лишились трех жизней. Текущее здоровье:", health-3)
        return health-3

def moving(x, y):
    for i_row in range (n):
        stroka=''
        for i_col in range (m):
            if (i_row==y) and (i_col==x):
                stroka=stroka+' *'
            else:
                stroka=stroka+' .'
        print (stroka)
            
def trap (health):###ловушка
    print ("Вы попали в комнату с ловушкой и лишились жизни")
    print ("Текущее здоровье:", health-1)
    return health-1 

x=0
y=0
print ('Ваше положение в игре будет отображаться звездочкой',
       'Управляйте своими движениями с помощью wasd. Будьте аккуратны и не врезайтесь в бортики')
moving (x, y)
while (otvet!=1 and health>0):
    print ('Делайте ваш ход')
    move=input()
    if move=='w' and y>0:
        y=y-1
    elif move=='s' and y+1<n:
        y=y+1
    elif move=='a' and x>0:
        x=x-1
    elif move=='d' and x+1<m:
        x=x+1
    moving (x, y)
    if (labirint[n*y+x]=='empty'):
        (empty())
    elif (labirint[n*y+x]=='mnstr'):
        health=monstr(things, health)
    elif (labirint[n*y+x]=='box'):
        health=box(health)
        labirint[n*y+x]='empty'
    elif (labirint[n*y+x]=='trap'):
        health=trap(health)
    elif (labirint[n*y+x]=='key'):
        (key(things))
        labirint[n*y+x]='empty'
    elif (labirint[n*y+x]=='exits'):
        otvet=exits(things)
if otvet==1:
    print ("Поздравляю вас с победой")
if health<=0:
    print ("Game over")





        
