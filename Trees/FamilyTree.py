def fn(level, pos):
    if bin(pos-1).count('1') % 2:
        return 'Doctor'
    else:
        return 'Engineer'
