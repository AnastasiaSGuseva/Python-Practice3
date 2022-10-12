# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

numb = int(input('Введите число: '))
r = range(-numb, numb + 1)
neg_fib = []


def n_fib(n):
    if n < 0:
        if n == -1:
            return 1
        elif n == -2:
            return -1
        else:
            return n_fib(n + 2) - n_fib(n + 1)
    if n >= 0:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            return n_fib(n - 1) + n_fib(n - 2)


for i in r:
    neg_fib.append(n_fib(i))
print(neg_fib)
