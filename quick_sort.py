num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

# Quick Sort
def quickSort(num, left, right):
    if left < right:
        partition_pos = partition(num, left, right)
        quickSort(num, left, partition_pos - 1)
        quickSort(num, partition_pos + 1, right)


def partition(num, left, right):
    i = left
    j = right
    pivot = num[right]

    while i < j:
        while i < right and num[i] < pivot:
            i += 1
        
        while j > left and num[j] >= pivot:
            j -= 1

        if i < j:
            num[i], num[j] = num[j], num[i]

    if num[i] > pivot:
        num[i], num[right] = num[right], num[i]

    return i

quickSort(num, 0, len(num) - 1)
print(num)