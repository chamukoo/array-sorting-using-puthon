num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

print("\n\n\n" + ("="*56) + "\n\n\t\t   ⭐  BUBBLE SORT  ⭐\n\n" + ("="*56))

# Bubble Sort
def bubbleSort(num):

    for i in range(len(num) -1, 0, -1):
        for j in range(i):
            if num[j] > num[j + 1]:
                temp = num[j] 
                num[j] = num[j + 1]
                num[j + 1] = temp

                print("\n", "\t", num, "\n\n", ("-")*56, "\n\n")

bubbleSort(num)