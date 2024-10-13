def fib(n):

    if n == 0:
        return 0
    
    if n <= 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)

#time complexity: O(2^n)
#space complexity: O(n)
def main():
    print(fib(3))
    print(fib(7))
    print(fib(0))
    print(fib(1))

if __name__ == "__main__":
    main()