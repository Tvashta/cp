# Since you became a director of a large company, you came to know all of your n employees perfectly well.
# You carefully studied their relationships and came up with a list of pairs of workers who respect one another.
# You are sure that in a healthy environment subordinates should respect their immediate superiors,
# which is why you would like to change the hierarchy in the company according to the list you composed.
# This hierarchy should be represented by a rooted tree, and for each pair of employees a, b,
# a is an immediate superior of b (or the other way round) if and only if a respects b and vice versa.

# Given the number of people in you company n and the respectList you created,
# calculate the number of different hierarchies you can create.

# Basically count number of spanning trees
# Kirchoff's algorithm:
# Subtract adj matrix from degree matrix [Diagnals with degree and edges with -1] and cofactor gives the number of spanning trees

def hierarchiesCount(n, respectList):
    MOD = 10**9 + 7
    if n == 1:
        return 1
    A = [[0] * n for _ in range(n)]
    for i, j in respectList:
        A[i][i] += 1
        A[j][j] += 1
        A[i][j] = A[j][i] = -1
    return (det(A) * n) % MOD


def det(A):
    N = len(A)
    for i in range(N-2):
        for j in range(i+1, N):
            for k in range(i+1, N):
                A[j][k] = A[j][k] * A[i][i] - A[j][i] * A[i][k]
                if i:
                    A[j][k] /= A[i-1][i-1]
    return A[-2][-2]
