import math
class Kalkulator:
    def __init__(self, num_1=None, num_2=None, num_3=None):
        self.num_1=num_1
        self.num_2=num_2
        self.num_3=num_3
    def usual_kal(self, num_1, num_2, znak):
        if znak==1:
            return (num_1+num_2)
        elif znak==2:
            return (num_1-num_2)
        elif znak==3:
            return (num_1*num_2)
        elif znak==4:
            return (num_1/num_2)
        else:
            return ('Ошибка ввода')
    def ing_kal (self, num_3, function):
        if function==1:
            return math.sin(num_3)
        if function==2:
            return math.cos(num_3)
print ('Если хотите использовать обычный калькулятор, введите 1. Если инженерный - введите 2')
type_kal=int(input())
if type_kal==1:
    print ('Введите два числа. Каждое с новой строки')
    number_1=float(input())
    number_2=float(input())
    print ('Если хотите сложить числа, введите 1; если получить их разность, введите 2; если произведение - 3; если частное - 4')
    znak=int(input())
    base=Kalkulator(num_1=number_1, num_2=number_2)
    print (base.usual_kal(number_1, number_2, znak))
if type_kal==2:
    print ('Введите число')
    number_3=float(input())
    print ('Если хотите получить синус числа, введите 1. Для получения косинуса введите 2')
    function=int(input())
    ingener=Kalkulator(num_3=number_3)
    print (ingener.ing_kal (number_3, function))
    
