from test_framework import generic_test


def fibonacci(n: int) -> int:
    # TODO - you fill in here.
    curr = 1
    prev = 1
    if n == 0:
        return 0
    if n == 1:
        return curr
    for i in range(2, n):

        curr, prev = curr + prev, curr

    return curr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
