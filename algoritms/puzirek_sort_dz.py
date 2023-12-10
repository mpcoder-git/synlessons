#Модернизировать алгоритм сортировки пузырьком так, чтобы небыло лишних проходов цикла при отсортированом списке
import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
issorted = True


print('not sorted:')
print(arr)

for i in range(n):
    for j in range(n - 1):
        left = arr[j]
        right = arr[j + 1]
        if left > right:
            arr[j] = right
            arr[j+1] = left
            issorted = False
            print(arr)
    #Если закончились сравнения, то выходим из цикла
    if (issorted is True):
        break
    else:
        issorted = True        


print('sorted:')
print(arr)
