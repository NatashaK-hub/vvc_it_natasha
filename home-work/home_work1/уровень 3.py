def kalkulator_num (num_1, num_2: int):
    print ('Если хотите сложить числа, введите 1; если получить их разность, введите 2; если произведение - 3; если частное - 4')
    znak=int(input())
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
print ('Введите два целых числа:')
a=int(input())
b=int(input())
print (kalkulator_num(a, b))
