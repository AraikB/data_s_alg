# python3

from random import randint


def partition3(array, left, right):
    lesser = left  # We initiate lesser to be the part that is less than the pivot
    i = left   # We scan the array from left to right
    greater = right  # The part that is greater than the pivot
    pivot = array[left]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= greater:      # Starting from the first element.
        if array[i] < pivot:
            array[lesser], array[i] = array[i], array[lesser]
            lesser += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[greater] = array[greater], array[i]
            greater -= 1
        else:
            i += 1
            
    return lesser, greater


def randomized_quick_sort(array, left, right):
    if left >= right:
        return left
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    lesser, greater = partition3(array,left,right)
    randomized_quick_sort(array, left, lesser-1)
    randomized_quick_sort(array,greater+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
