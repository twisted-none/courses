# Назовем число несчастливым если его простые множители включают только 2, 3 и 5.
# Напишите программу, которая определяет является ли введенное число несчастливым или нет.


def d(n):
    lst = [i for i in range(2, int(n**0.5)+1)]
    lst1 = []
    for i in lst:
        if n % i == 0:
            if i > 5:
                lst1.append(i)
            if n // i > 5:
                lst1.append(n//i)
    return lst1

def resheto(n):
    lst = d(n)
    lst1 = []
    for i in range(len(lst)):
        for j in range(2, int(lst[i]**0.5) + 1):
            if lst[i] % j == 0:
                break
        else:
            lst1.append(lst[i])
    return lst1

n = int(input())
resheto_lst = resheto(n)
for i in resheto_lst:
    if n % i == 0:
        print('NO')
        break
else:
    if n != 1:
        print('YES')
    else:
        print('NO')