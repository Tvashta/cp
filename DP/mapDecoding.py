# A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent and you need to determine the total number of ways that the message can be decoded.
# Since the answer could be very large, take it modulo 109 + 7.

def mapDecoding(m):
    mod = 10**9 + 7
    n = len(m)
    if not len(m):
        return 1
    f = 1
    for i in range(n):
        if m[i] == '0':
            if i-1 >= 0 and m[i-1] <= '2' and m[i-1] >= '1':
                continue
            else:
                f = 0
                break
    if not f:
        return 0
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if m[i-1] > '0':
            dp[i] = dp[i-1]
        if m[i-2] == '1' or (m[i-2] == '2' and m[i-1] < '7'):
            dp[i] += dp[i-2] % mod
    return dp[n] % mod


# Space optimized
def map(m):
    mod = 10**9 + 7
    if not len(m):
        return 1
    if m[0] == '0':
        return 0
    x, y = 1, 1
    for i in range(1, len(m)):
        z = 0
        if m[i] != '0':
            z += y
        if m[i-1] == '1' or (m[i-1] == '2' and m[i] < '7'):
            z += x
        x, y = y, z % mod
    return y


# Clean python code
def mapClean(m):
    mod = 10**9+7
    a, b = 1, 0
    for i in range(len(m)-1, -1, -1):
        if m[i] == '0':
            a, b = 0, a
        else:
            a, b = (a + (i+2 <= len(m) and m[i:i+2] <= '26')*b) % mod, a
    return a
