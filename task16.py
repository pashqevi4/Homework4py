# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint


N = int(input())
list_1 = []
for i in range(N):
    list_1.append(randint(1, 9))

print(*list_1)

X = int(input())

count = 0

for i in range(N):
    if list_1[i] == X:
        count +=1
    
            
print(f'-->{count}')
