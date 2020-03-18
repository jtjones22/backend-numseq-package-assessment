def fib(n):
    """Compute the nth term of fibonacci sequence"""
    num_1 = 0
    num_2 = 1
    result = 0
    if n == 1:
        return 1
    else:
        for num in range(1, n):
            result = num_1 + num_2
            num_1 = num_2
            num_2 = result
        return result


if __name__ == '__main__':
    fib(5)