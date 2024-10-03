def gridTraveler(m, n, memo = {}):
    key = m + ',' + n
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler((m - 1), n , memo) + gridTraveler(m, (n - 1), memo)
    return memo[key]

    # Time complexity O(m * n), Space complexity O(m + n)

def main():
    print(gridTraveler(0,1))
    print(gridTraveler(1,1))
    print(gridTraveler(2,3))
    print(gridTraveler(3,2))
    print(gridTraveler(3,3))
    print(gridTraveler(18,18))

if __name__ == "__main__":
    main()
