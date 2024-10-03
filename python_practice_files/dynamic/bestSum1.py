def bestSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    bestCombination = None

    for number in numbers:
        remainder = targetSum - number
        remainderCombo = bestSum(remainder, numbers, memo)
        if remainderCombo is not None:
            combination = remainderCombo + [number]
            if bestCombination is None or len(combination) < len(bestCombination):
                bestCombination = combination

    memo[targetSum] = bestCombination
    return bestCombination

# m = targetSum
# n = len(numbers)
# Time complexity O(n * m * m), Space complexity O(m * m)

def main():
    print(bestSum(7, [5, 4, 3, 7]))
    print(bestSum(7, [5, 4, 3, 7]))
    print(bestSum(8, [1, 4, 5])) 
    print(bestSum(7, [2, 4]))  
    print(bestSum(0, [1, 2, 3]))  
    print(bestSum(100, [1, 2, 5, 25]))  

if __name__ == "__main__":
    main()