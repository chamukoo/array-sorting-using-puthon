num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

print(num)
print("\n\n\n" + ("="*56) + "\n\n\t\t  ⭐  MERGE SORT  ⭐\n\n" + ("="*56))

# Merge Sort
def mergeSort(num):
    if len(num) > 1:
        left = num[:len(num)//2]
        right = num[len(num)//2:]

        # Recursion
        mergeSort(left)
        mergeSort(right)

        # Merge
        i = 0 # left index
        j = 0 # right index
        k = 0 # merge array index

        while i < len(left) and j < len(right):
            if left[i] <  right[j]:
                num[k] = left[i]
                i += 1
            else:
                num[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num[k] = right[j]
            j += 1
            k += 1

        print("\n", "\t", num, "\n\n", ("-")*56, "\n")

mergeSort(num)