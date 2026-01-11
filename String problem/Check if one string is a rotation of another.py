def nth_fibonacci_loop(n, memo):

    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)

    return memo[n]


def nth_fibonacci(n):
    memo = [-1] * (n + 1)

    return nth_fibonacci_loop(n, memo)


if __name__ == "__main__":
    n = 5
    result = nth_fibonacci(n)
    print(result)