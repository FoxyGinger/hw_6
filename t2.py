# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


from random import randint

nums = [randint(0, 20) for _ in range(randint(10, 15))]
min, max = randint(0, 10), randint(10, 20)

print(nums)
print(f'Минимальное число: {min}')
print(f'Максимальное число: {max}')

result = []

for i in range(len(nums)):
    if min <= nums[i] <= max:
        result.append(i)

print(result)