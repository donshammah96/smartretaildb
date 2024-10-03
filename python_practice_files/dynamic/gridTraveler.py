def gridTraveler(m, n, memo = {}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m, n)] = gridTraveler((m - 1), n, memo) + gridTraveler(m, (n - 1), memo)
    return memo[(m, n)]

def main():
    print(gridTraveler(0,1))
    print(gridTraveler(1,1))
    print(gridTraveler(2,3))
    print(gridTraveler(3,2))
    print(gridTraveler(3,3))
    print(gridTraveler(18,18))

if __name__ == "__main__":
    main()