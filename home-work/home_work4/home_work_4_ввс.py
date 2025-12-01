import pandas as pd
import numpy as np

titanic=pd.read_csv('tested.csv')
print (titanic)

print ("Определение пропусков:")
#isnull()- определение пропусков
print (titanic.isnull().sum())

print("Тип данных:")
#dtypes-показывает тип данных каждого из столбцов
print(titanic.dtypes)

#titanic.info()) - общая информация, включая кол-во непустых значений

#print ("Введите количество строк, которое нужно вывести")
#n=int(input())
n=3
print ("Первые ", n, " строк:")
#head - метод, возвращает первые n строк
print(titanic.head(n))

print("Последние три строки:")
#tail(n)- метод, возвращает последние n строк
print (titanic.tail(3))

print ("Базовая статистика по числовым столбцам:")
#describe()-показывает среднее, минимальное, максимальное, std-отклонения
print (titanic.describe())

print ("количество заголовков (столбцов):")
print (titanic.columns.size)
#titanic.columns - перечисление всех столбцов
print (titanic.columns)

print("Количество строк:")
print (len(titanic))

print ("Общее количество пропусков:")
print (titanic.isnull().sum().sum())
mode_age=titanic["Age"].mode()[0]
#[0] - обращение к первому элементу Series, состоящему из самых популярных значений (мод)
titanic["Age"].fillna(mode_age, inplace=True)
#-> замена в стобце age пустых значений (True) модой
print ("Количество пропусков после замены:")
print (titanic.isnull().sum().sum())
row_nulls=titanic[titanic.isnull().any(axis=1)]
#строки, в которых есть ходя бы один пропуск (axis=1)
titanic_clean=titanic.drop(row_nulls.index[:20])
#удаление первых двадцати строк с пропусками

print ("После удаления 20 строк с пропусками:")
print (titanic_clean)

#сравнение двух групп между собой
tit_male=titanic[(titanic["Sex"]=="male")]
tit_female=titanic[(titanic["Sex"]=="female")]
tit_male_sur=tit_male[(tit_male["Survived"]==1)]
tit_female_sur=tit_female[(tit_female["Survived"]==1)]
tit_male_died=tit_male[(tit_male["Survived"]==0)]
tit_female_died=tit_female[(tit_female["Survived"]==0)]
print ("Доля выживших мужчин:", tit_male["Survived"].mean()*100, "%")
print ("Доля выживших женщин:", tit_female["Survived"].mean()*100, "%")
print ("Средний возраст мужчин:", tit_male["Age"].mean())
print ("Средний возраст женщин:", tit_female["Age"].mean())
print ("Средний возраст выживших мужчин:", tit_male_sur["Age"].mean())
print ("Средний возраст выживших женщин:", tit_female_sur["Age"].mean())
print ("Средний возраст погибших мужчин:",tit_male_died["Age"].mean())
print ("Средний возраст погибших женщин:",tit_female_died["Age"].mean())

#фильтрация
print ("Мужчины старше 30 лет, путешествующие 1-м классом:")
filtr_1=titanic[(titanic["Sex"]=="male") & (titanic["Age"]>30) & (titanic["Pclass"]==1)]
print (filtr_1)

print ("Моложе 18 лет ИЛИ женщины, при этом выжили:")
filtr_2=titanic[(titanic["Survived"]==1) & ((titanic["Age"]<18) | (titanic["Sex"]=="female"))]
print (filtr_2)

print ("Группировка по классу и полу:")
result=titanic.groupby(['Pclass', 'Sex']).agg({'Age': 'mean','Survived': 'mean',
                                              'Fare': 'mean'})
#groupby(['Pclass', 'Sex']) - список колонок, по которым мы группируем
#reset_index()- преобразует индекс обратно в колонки - можно добавить в конец
#agg - агрегировать, суммировать
#agg()-применить функцию/функции к данным
print (result)