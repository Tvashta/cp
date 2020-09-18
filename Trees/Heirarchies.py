# Since you became a director of a large company, you came to know all of your n employees perfectly well.
# You carefully studied their relationships and came up with a list of pairs of workers who respect one another.
# You are sure that in a healthy environment subordinates should respect their immediate superiors,
# which is why you would like to change the hierarchy in the company according to the list you composed.
# This hierarchy should be represented by a rooted tree, and for each pair of employees a, b,
# a is an immediate superior of b (or the other way round) if and only if a respects b and vice versa.

# Given the number of people in you company n and the respectList you created,
# calculate the number of different hierarchies you can create.
def hierarchiesCount(n, respectList):
    respectList = list(set(respectList))
