"""
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return None.
If there are multiple combinations possible, you may return any single one.

howSum(7, [5, 4, 3, 7]) -> [4, 3]
howSum(7, [5, 4, 3, 7]) -> [7]
howSum(8, [2, 3, 5]) -> [2, 2, 2, 2]
howSum(8, [2, 3, 5]) -> [3, 5]
howSum(7, [2, 4]) -> null
howSum(0, [1, 2, 3]) -> []

"""

def howSum(targetSum, numbers):

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for number in numbers:
        remainder = targetSum - number
        result = howSum(remainder, numbers)
        if result is not None:
            return result + [number]
        
    return None

# m = targetSum, n = len(numbers)
# Time complexity O(n^m * m), Space complexity O(m)

def main():
    print(howSum(7, [5, 4, 3, 7]))
    print(howSum(7, [2, 3]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(7, [2, 4]))
    print(howSum(0, [1, 2, 3]))
    print(howSum(300, [7, 14]))

if __name__ == "__main__":
    main()