def nextLarger(a):
    l = [-1]*len(a)
    stack = [0]
    for i in range(1, len(a)):
        while len(stack) and a[i] > a[stack[-1]]:
            l[stack[-1]] = a[i]
            stack.pop()
        stack.append(i)
    return l
