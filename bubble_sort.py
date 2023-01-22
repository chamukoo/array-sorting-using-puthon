num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

# Bubble Sort
def bubbleSort(num):

    for i in range(len(num) - 1, 0, -1):
        for j in range(i):
            if num[j] > num[j + 1]:
                temp = num[j + 1] 
                num[j + 1] = temp

bubbleSort(num)
print(num)