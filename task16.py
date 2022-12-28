# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2
import random
print('Введите количество элементов массива')
n = int(input())
print('Введите искомое число')
x = int(input())
a = []

def FindNum(arg1, arg2, arg3):
    count = 0
    for i in range(0, arg2):
        random_number = random.randint(1, arg2/2)
        arg1.append(random_number)
        if arg1[i] == arg3:
            count += 1
        if count == 0:
            print("Число не встретилось, не фартануло =( Попробуйте снова!)")
            break
    print(arg1)
    return count

arg1 = a
arg2 = n
arg3 = x
print(FindNum(arg1, arg2, arg3))
