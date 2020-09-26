# Given a string representing the file system in this format,
# return the length of the longest absolute path to a file in the abstracted file system.
# If there is not a file in the file system, return 0.

# The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:
# user
#    pictures
#        photo.png
#         camera
#     documents
#        lectures
#            notes.txt
# The directory user contains two sub-directories pictures and documents.
# pictures contains a file photo.png and an empty second-level sub-directory camera.
# documents contains a second-level sub-directory lectures containing a file notes.txt.
# We want to find the longest(as determined by the number of characters) absolute path to a file within our system.
# For example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt",
# and its length is 33 (not including the double quotes).


# Approach:
# Number of tabs gives the depth of each item
# Keep track of parent depth using dict at each step
# Maxlen should be calculated only for files so . must be there in it
# Length increases by 1 with depth as / is added after a dir

from collections import defaultdict


def longestPath(f):
    f = f.split('\n')
    m = 0
    path = defaultdict(lambda: 0)
    for i in f:
        s = i.lstrip('\t')
        depth = len(i)-len(s)
        if '.' in s:
            m = max(m, path[depth]+len(s))
        else:
            path[depth+1] = path[depth]+len(s)+1
    return m
