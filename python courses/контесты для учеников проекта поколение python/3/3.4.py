# На вход программе подается положительное целое число n, состоящее только из цифр 6 и 9. 
# Напишите программу, которая возвращает максимальное число, 
# которое вы можете получить, изменив не более одной цифры (6 заменяется на 9, а 9 на 6).

n = list(input())

if '6' in n:
    n[n.index('6')] = '9'
print(''.join(n))