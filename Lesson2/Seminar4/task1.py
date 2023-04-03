# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

m = int(input("Введите количество элементов первого множества: "))
n = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

a = [int(x) for x in input("Введите элементы первого множества: ").split()]
b = [int(x) for x in input("Введите элементы второго множества: ").split()]

set1 = set(a)
set2 = set(b)

unionSet = set1.union(set2)
c = list(unionSet)
c.sort()
unioinSet = set(c)
print(unionSet)