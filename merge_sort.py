num = [70, 83, 10, 38, 56,	49,	16,	32,	45,	63]

def mergeSort(num, left, right):
    if left >= right:
        return
    
    mid = (left + right) // 2

    mergeSort(num, left, mid)
    mergeSort(num, mid + 1, right)

    merge(num, left, right, mid)


def merge(num, left, right, mid):
    left_cpy = num[left:mid + 1]
    right_cpy = num[mid + 1:right + 1]

    l_counter = 0
    r_counter = 0
    sorted_counter = left

    while l_counter < len(left_cpy) and r_counter < len(right_cpy):
        if left_cpy[l_counter] <= right_cpy[r_counter]:
            num[sorted_counter] = left_cpy[l_counter]
            l_counter += 1

        else:
            num[sorted_counter] = right_cpy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_cpy):
        num[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_cpy):
        num[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
        sorted_counter += 1

print(num)

mergeSort(num, 0, len(num) - 1)
print(num)