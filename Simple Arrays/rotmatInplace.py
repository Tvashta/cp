def rot(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if i > j:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    for i in range(n):
        for j in range(n//2):
            a[i][j], a[i][n-j-1] = a[i][n-j-1], a[i][j]
    return a
