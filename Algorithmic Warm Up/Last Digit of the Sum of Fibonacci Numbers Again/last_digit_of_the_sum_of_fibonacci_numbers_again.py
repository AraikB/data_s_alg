# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    f = [0, 1]

    if from_index > 1000:
        from_index=int(from_index%60)

    if to_index > 1000:
        to_index=int(to_index%60)

    def reduce_from(from_index):
        if from_index <= 70:
            return int(from_index)
        else:
            from_index=from_index-60
            reduce_from(from_index)
        return from_index

    def reduce_toind(to_index):
        if to_index <= 70:
            return int(to_index)
        else:
            to_index = to_index-60
            reduce_toind(to_index)
        return to_index

    from_index = reduce_from(from_index)
    to_index = reduce_toind(to_index)

    if from_index>to_index:
        to_index = to_index+60

    for i in range(2, (to_index)+4):
        f.append(f[i-1] + f[i-2])

    result = (f[to_index+2]-f[from_index+1])

    return result%10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
