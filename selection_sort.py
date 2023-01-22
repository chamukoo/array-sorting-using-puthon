num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

# Selection Sort
def selectionSort(num):

    for i in range(9):
        minpos = i

        for j in range(i, 10):
            if num[j] < num[minpos]:
                minpos = j

        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp

        print(num)

selectionSort(num)
print(num)