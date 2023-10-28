# Последовательность Трибоначчи Tn определяется следующим образом: T0=0, T1=1,T2=1 для n≥0.
# Напишите программу, которая вычисляет n-ое число последовательности Трибоначчи.


from functools import lru_cache

@lru_cache()
def fibonacci(n):
    if n in (1, 2):
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 3) + fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(int(input())))