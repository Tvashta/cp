# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution.
# The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted
# as the word1 + word2 = word3 cryptarithm.

# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution,
# becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true.
#  If it does not become a valid arithmetic solution, the answer is false.
def isCryptSolution(crypt, solution):
    a = {l[0]: int(l[1]) for l in solution}
    sum = [0]*3
    for it, i in enumerate(crypt):
        s = list(i)
        if len(s) > 1 and a[s[0]] == 0:
            return False
        n = 0
        for j in s:
            n *= 10
            n += a[j]
        sum[it] = n
    return sum[0]+sum[1] == sum[2]


# A super cute magical solution
def cute(crypt, sol):
    d = {ord(c): d for c, d in sol}
    *v, = map(lambda x: x.translate(d), crypt)
    return not any(i != '0' and i.startswith('0') for i in v) and int(v[0])+int(v[1]) == int(v[2])
