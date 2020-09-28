# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode(s):
    if not s:
        return 0
    dp = [0]*(len(s)+1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0
    for i in range(2, len(s)+1):
        if '0' < s[i-1] <= '9':
            dp[i] += dp[i-1]
        if s[i-2] == '1' or (s[i-2] == '2' and '0' <= s[i-1] <= '6'):
            dp[i] += dp[i-2]
    return dp[len(s)]
