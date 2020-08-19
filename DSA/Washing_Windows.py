t = int(input())
while t > 0:
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    dp = [[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = l[i][j]
            else:
                if j == 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j+1], l[i][j])
                elif j == m-1:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], l[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j],
                                   dp[i-1][j+1], l[i][j])

    for i in range(n):
        for j in range(m):
            if l[i][j] >= dp[i][j]:
                print(1, end="")
            else:
                print(0, end="")
        print()
    t -= 1
