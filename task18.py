# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint

N = int(input())
list_1 = []

for i in range(N):
    list_1.append(randint(1, 50))

print(*list_1)

X = int(input())
neighbor = list_1[0]
summ = abs(X - list_1[0])

for i in range(0, N):
    if abs(X - list_1[i]) < summ:
        summ = abs(X - list_1[i])
        neighbor = list_1[i]
print(f'самое близкое по значению число {neighbor}')
