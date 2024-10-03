def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
        
    memo[targetSum] = False
    return False

    # Time complexity O(n * m), Space complexity O(m)

def main():
    print(canSum(7, [2, 3]))  # True
    print(canSum(7, [5, 4, 3, 7]))  # True
    print(canSum(7, [2, 4]))  # False
    print(canSum(8, [2, 3, 5]))  # True
    print(canSum(300, [7, 14]))  # False

if __name__ == "__main__":
    main()