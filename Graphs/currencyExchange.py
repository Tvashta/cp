# Question:
# A currency converter has the exchange rates exchange,
# such that exchange[i][j] represents the amount of money you would get for exchanging
# 1 unit of the ith currency for 1 unit of the jth currency.
# A "non-exchange" (that is , exchanging a currency with itself) is represented by exchange[i][i] = 1.
# Write a function that returns True if it's possible to make money by doing a series of exchanges
# (i.e. to start with some currency C and to end with a greater amount of currency C after a series of exchanges),
# and False otherwise.

# Clue given is that we need to do this in O(n^3)
# My approach would be to use Floyd Warshall's all pairs shortest path algorithm
# If the shortest path from a currency to another is >1 return True

def currencyArbitrage(exchange):
    n = len(exchange)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                exchange[i][j] = max(
                    exchange[i][k]*exchange[k][j], exchange[i][j])
    for i in range(n):
        if exchange[i][i] > 1:
            return True
    return False
