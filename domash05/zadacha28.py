# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a
print(sum(2, 2))