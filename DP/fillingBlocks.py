# You have a block with the dimensions 4 × n.
# Find the number of different ways you can fill this block with smaller blocks that have the dimensions 1 × 2.
# You are allowed to rotate the smaller blocks.
def fillingBlocks(n):
    if n <= 1:
        return n
    elif n == 2:
        return 5
    elif n == 3:
        return 11
    elif n == 4:
        return 36
    else:
        dp = [0]*(n+1)
        dp[1], dp[2], dp[3], dp[4] = 1, 5, 11, 36
        for i in range(5, n+1):
            dp[i] = dp[i-1]+5*dp[i-2]+dp[i-3]-dp[i-4]
        return dp[n]
