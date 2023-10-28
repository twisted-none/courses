# На вход подается строка, состоящая из целых чисел, разделенных пробелами.
# Назовем число счастливым если его частота появления в строке равна его значению.
# Напишите программу, которая выводит самое большое счастливое число в заданной строке.

s = list(map(int, input().split()))

s_count_numb = dict()

for i in s:
    if i not in s_count_numb:
        s_count_numb[i] = s.count(i)


max_lucky_num = -1

for x, y in s_count_numb.items():
    if i == s_count_numb[i]:
        max_lucky_num = i
print(max_lucky_num)