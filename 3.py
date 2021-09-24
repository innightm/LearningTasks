import random
mas = []
sum = 0
# Генерируем массив из 10 чисел от 1 до 10:
mas = [random.randint(1,10) for i in range(1,10)]
print(mas)
# Проходим в цикле по массиву и все четные числа суммируем:
for i in mas:
    if (i%2) == 0:
        sum += i
print(sum)
input ("\nДля выхода, нажмите Ввод...")
