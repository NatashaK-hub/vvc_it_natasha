def sum_num (num_1, num_2: int):
    s = num_1+num_2
    return int(s)
def raznost_num (num_1, num_2: int):
    r = num_1-num_2
    return int(r)
def proizvedenie_num (num_1, num_2: int):
    p = num_1*num_2
    return int (p)
def chastnoe_num (num_1, num_2: int):
    ch = num_1/num_2
    return float (ch)
print ('Введите два целых числа:')
a=int(input())
b=int(input())
print ('Если хотите сложить числа, введите 1; если получить их разность, введите 2; если произведение - 3; если частное - 4')
znak=int(input())
if znak==1:
    print ('Ответ:', sum_num(a, b))
elif znak==2:
    print ('Ответ:', raznost_num(a, b))
elif znak==3:
    print ('Ответ:', proizvedenie_num (a, b))
elif znak==4:
    print ('Ответ:', chastnoe_num(a, b))
else:
    print ('Ошибка ввода')
