"""
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10

"""

a = int(input('Введите число: '))
b = a
osn = 2
ost = []


while a != 0:
    ost.append(str(a % 2))
    a = a // osn


ost.reverse()
ost_str = "".join(ost)
print(f'{b}'u'\u2081\u2080', end=' = ')
print(f'{ost_str}'u'\u2082')
