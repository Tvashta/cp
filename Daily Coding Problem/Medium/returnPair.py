# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# Implement car and cdr.
# This is my first functional programming sorta problem.
# Here f is the function passed in pair. So if I do
# d=cons(a,b)
# d(print)
# a,b will be printed on the screen
d = cons(1, 2)
print(d)
d(print)
print(d(print))
