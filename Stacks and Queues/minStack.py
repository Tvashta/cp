# O(n) space [Not altering original Stack]
def minimumOnStack(operations):
    stack = []
    minStack = []
    op = []
    for i in operations:
        if i == 'min':
            if minStack:
                op.append(minStack[-1])
        elif i == 'pop':
            if stack:
                stack.pop()
                minStack.pop()
        else:
            i = i.split()
            x = int(i[1])
            stack.append(x)
            if minStack:
                minStack.append(min(minStack[-1], x))
            else:
                minStack.append(x)
    return op

# O(1) space
