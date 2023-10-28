# На вход подаются строки a и b. 
# Напишите программу, которая определяет, является ли строка a подпоследовательностью строки b.

first_str, second_str = input(), input()

i_found = 0


if first_str != second_str:
    for i in range(len(first_str)):
        for j in range(i_found, len(second_str)):
            if first_str[i] == second_str[j]:
                i_found = j + 1
                break
        else:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')