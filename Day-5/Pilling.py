def piling_up(blocks):
    left = 0
    right = len(blocks) - 1
    last = float('inf')

    while left <= right:
        if blocks[left] >= blocks[right]:
            pick = blocks[left]
            left += 1
        else:
            pick = blocks[right]
            right -= 1

        if pick > last:
            return "No"
        last = pick

    return "Yes"


# Input handling
T = int(input("Enter the value of t"))
for _ in range(T):
    n = int(input("Enter the value of n"))
    blocks = list(map(int, input("Enter the element").split()))
    print(piling_up(blocks))