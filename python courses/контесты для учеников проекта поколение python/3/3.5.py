# На вход программе подается строка. Напишите программу, которая "переворачивает" строку в соответствии с правилами:
# все символы, не являющиеся буквами, остаются на своих местах;
# все буквы меняют свой порядок на обратный.
# Sample Input 2:
# a+b-c=abc
# Sample Output 2:
# c+b-a=cba

n = list(input())

lst_of_symb = []

for i in range(len(n)):
    if n[i].isalpha(): 
        lst_of_symb.append(n[i])
        n[i] = 'z'
lst_of_symb = lst_of_symb[::-1]

numb_of_replaces = 0
for j in range(len(n)):
    if n[j].isalpha():
        n[j] = lst_of_symb[numb_of_replaces]
        numb_of_replaces += 1

print(''.join(n))
