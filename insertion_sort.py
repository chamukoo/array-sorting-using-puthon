num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

def insertionSort(num):
    for i in range(1, len(num)):
        j = i

        while num[j - 1] > num[j] and j > 0:
            num[j - 1], num[j] = num[j], num[j - 1]
            j -= 1

            print(num)

insertionSort(num)
print(num)
