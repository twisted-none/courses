# На вход программе подается натуральное число n, а затем n телефонных номеров, каждый на отдельной строке. 
#Необходимо вывести те номера, которые являются корректными.
#Корректными номерами будут номера следующих двух форматов: 
#(xxx) xxx-xxxx
#xxx-xxx-xxxx
#где x – цифра от 0 до 9.

from fnmatch import fnmatch as fn

lst_of_numbers = [input() for _ in range(int(input()))]
c = 0
for i in lst_of_numbers:
    if fn('(???) ???-???', i) or fn('???-???-????', i):
        c += 1
        print(i)

if not c:
    print('All phone numbers are incorrect')