#интерполяционный поиск
import random

n = 500
arr = list()
#параметр сортировка указывает на то, что произошла сортировка. 
# Нужен во избежании лишних проходов

to_search = 45
answer = -1

''' 
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
'''

arr = [1,10,45,67]

print(to_search)
print(arr)


#---------------------------------------

left = 0
right = len(arr) - 1
while (left <= right and to_search >= arr[left] and to_search <= arr[right]):
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_search - arr[left]

    index = left + int(part1 * part2)

    if arr[index] == to_search:
        answer = index
        break
    if arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1




#---------------------------------------

if answer != -1:
    print(f"Элемент в списке есть, его индекс: {answer}")
else:
    print(f"Элемент в списке нет")



