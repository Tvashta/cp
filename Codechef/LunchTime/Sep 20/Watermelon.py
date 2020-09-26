# def fn(s, a, i):
#     if s >= i and a[i-1] >= i and i >= 0:
#         s -= i
#         a[i-1] -= i
#         if s == 0:
#             return True
#         b = a.copy()
#         return fn(s, b, i) or fn(s, b, i-1)
#     return False


t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if s == 0:
        print('YES')
    elif s < 0:
        print('NO')
    else:
        if n == 1:
            print('YES')
        elif n == 2:
            if s % 2:
                if (s <= a[0] and a[0] > 0) or (s/2 <= a[1] and a[1] > 0):
                    print('YES')
                else:
                    print('NO')
            else:
                if a[0] < 0:
                    print('NO')
                elif a[0] >= s:
                    print('YES')
                else:
                    if a[1] < 0:
                        print('NO')
                    else:
                        if (s-1)/2 <= a[1]:
                            print('YES')
                        else:
                            print('NO')
        else:
            print('NO')
        # if fn(s, a, n):
        #     print('YES')
        # else:
        #     print('NO')
    t -= 1
