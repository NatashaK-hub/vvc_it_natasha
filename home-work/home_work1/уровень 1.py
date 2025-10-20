print ('Введите два целых числа:')
a=int(input())
b=int(input())
print ('Если хотите сложить числа, введите 1; если получить их разность, введите 2; если произведение - 3; если частное - 4')
znak=int(input())
if znak==1:
    print ('Ответ:', a+b)
elif znak==2:
    print ('Ответ:', a-b)
elif znak==3:
    print ('Ответ:', a*b)
elif znak==4:
    print ('Ответ:', a/b)
else:
    print ('Ошибка ввода')
    


