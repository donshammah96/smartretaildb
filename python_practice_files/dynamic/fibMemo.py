def fib(n, memo = None):
    if memo == None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

    #time complexity: O(n)
    #space complexity: O(n)
def main():
    print(fib(50))

if __name__ == "__main__":
    main()