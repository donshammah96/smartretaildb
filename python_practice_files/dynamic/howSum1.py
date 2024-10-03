
def howSum(targetSum, numbers, memo=None):

    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    for number in numbers:
        remainder = targetSum - number
        result = howSum(remainder, numbers, memo)
        if result is not None:
            memo[targetSum] = result + [number]
            return memo[targetSum]
        
    memo[targetSum] = None
    return None

    #Memoized solution

    # m = targetSum
    # n = len(numbers)
    # Time complexity O(n * m * m), Space complexity O(m * m)

def main():
    print(howSum(7, [5, 4, 3, 7]))
    print(howSum(7, [2, 3]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(7, [2, 4]))
    print(howSum(0, [1, 2, 3]))
    print(howSum(300, [7, 14]))

if __name__ == "__main__":
    main()