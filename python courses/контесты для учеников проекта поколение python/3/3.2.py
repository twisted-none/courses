# Последовательность Трибоначчи Tn определяется следующим образом: T0=0, T1=1,T2=1 для n≥0.
# Напишите программу, которая вычисляет n-ое число последовательности Трибоначчи.


from functools import lru_cache

@lru_cache()
def tribonacci(n):
    if n in (1, 2):
        return 1
    if n == 0:
        return 0
    return tribonacci(n - 3) + tribonacci(n - 1) + tribonacci(n - 2)
 
 
print(tribonacci(int(input())))