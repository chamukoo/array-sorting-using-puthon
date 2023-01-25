num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

print("\n\n\n" + ("="*56) + "\n\n\t\t⭐  INSERTION SORT  ⭐\n\n" + ("="*56))

# Insertion Sort
def insertionSort(num):
    for i in range(1, len(num)):
        j = i

        while num[j - 1] > num[j] and j > 0:
            num[j - 1], num[j] = num[j], num[j - 1]
            j -= 1

            print("\n", "\t", num, "\n\n", ("-")*56, "\n\n")

insertionSort(num)