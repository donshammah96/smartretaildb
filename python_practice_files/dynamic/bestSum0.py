"""
Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
If there is a tie for the shortest combination, you may return any one of the shortest.
If there is no combination that adds up to the targetSum, then return None.

bestSum(7, [5, 4, 3, 7]) -> [4, 3]
bestSum(7, [5, 4, 3, 7]) -> [7]
bestSum(8, [2, 3, 5]) -> [3, 5]
bestSum(7, [2, 4]) -> null
bestSum(0, [1, 2, 3]) -> []


"""

def bestSum(targetSum, numbers):

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    bestCombination = None

    for number in numbers:
        remainder = targetSum - number
        remainderCombo = bestSum(remainder, numbers)
        if remainderCombo is not None:
            combination = remainderCombo + [number]
            if bestCombination is None or (len(combination) < len(bestCombination)):
                bestCombination = combination
                
    return bestCombination          
        
# m = targetSum
# n = len(numbers)
# Time complexity O(n * m * m), Space complexity O(m * m)
        
def main():
    print(bestSum(7, [5, 4, 3, 7]))   
    print(bestSum(8, [1, 4, 5]))  
    print(bestSum(7, [2, 4]))  
    print(bestSum(0, [1, 2, 3]))  
    #print(bestSum(100, [1, 2, 5, 25])) 

if __name__ == "__main__":
    main()