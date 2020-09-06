def simplifyPath(path):
    path = path.split('/')
    newPath = []
    for i in path:
        if len(i) > 0 and i[0].isalpha():
            newPath.append(i)
        elif i == '..':
            if newPath:
                newPath.pop()
    newPath = '/'.join(newPath)
    return '/'+newPath
