# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    def merge_list(left,right):
        result = list()
        i,j = 0,0
        inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv_count += (len(left)-i)
        result += left[i:]
        result += right[j:]
        return result,inv_count

    def sort_and_count(array):
        if len(array) <= 1:
            return array, 0
        middle = len(array) // 2
        left,inv_left = sort_and_count(array[:middle])
        right,inv_right = sort_and_count(array[middle:])
        merged, count = merge_list(left,right)
        count += (inv_left + inv_right)
        return merged, count
    count = sort_and_count(a)
    return count[1]
if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
