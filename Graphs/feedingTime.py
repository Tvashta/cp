# Question:
# You have a list classes, such that classes[i] is a list of animals that the ith class wants to feed.
# Classes i and j cannot come on the same day if an animal in classes[i] also appears in classes[j](for i ≠ j).
# Your job is to determine the minimum number of days you would need to have all the classes come
# to feed the animals if they can all come within 5 days.
# If it isn't possible for all the classes to come within 5 days, return -1 instead.

# Greedy
# Basically each days animals must be unique as such
# So a defaultdict for each day and if they can't add to this day, just go to the next
# Greedy brute force won't work!
# A B C
# G H D
# D E F
# F I J

# According to our greedy algorithm,
# ABCGHD
# DEF
# FIJ
# 3

# Optimal solution is:
# ABCDEF
# GHDFIJ
# 2

# Optimal Solution:
# Graph coloring... How?
# Basically consider all the classes that have common animals as adjacent ones.
# Since they can't be visited in the same day. Now day becomes colors and
# Our problem can be solved with Backtracking
