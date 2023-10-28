# На вход программе подаются строки a и b. 
# Строка b генерируется случайным перемешиванием строки a с последующим добавлением символов в произвольных позициях.
# Напишите программу, которая вывыводит символы, которые были добавлены к строке b.

first_str, second_str = input(), input()

diff = ''
for i in range(len(second_str)):
    if second_str[i] not in diff:
        if second_str[i] not in first_str:
            diff += second_str[i] * second_str.count(i)
        else:
            diff += second_str[i] * (second_str.count(second_str[i]) - first_str.count(second_str[i]))
print(diff)