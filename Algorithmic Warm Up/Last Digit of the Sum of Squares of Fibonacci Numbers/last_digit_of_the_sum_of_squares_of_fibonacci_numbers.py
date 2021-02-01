# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    f = [0, 1]

    if n > 1000:
        n=int(n%60)

    def reduce_from(n):
        if n <= 70:
            return int(n)
        else:
            n=n-60
            reduce_from(n)
        return n

    n = reduce_from(n)

    for i in range(2, (n+4)):
        f.append(f[i-1] + f[i-2])
    result = f[n]*(f[n]+f[n-1])

    return result%10



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
