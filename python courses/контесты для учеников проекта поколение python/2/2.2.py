# На вход программе подается строка, состоящая из чисел, разделенных одним пробелом. 
# Необходимо переместить все числа 0 в конец, сохраняя относительный порядок ненулевых элементов. 

s = list(map(int, input().split()))

new_s = []

for i in s:
    if i != 0:
        new_s.append(i)

for i in range(len(s)-len(new_s)):
    new_s.append(0)

print(new_s)