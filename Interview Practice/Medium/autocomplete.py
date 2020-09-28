# Implement an autocomplete system.
# That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(lambda: Node())
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        cur = self.root
        for i in s:
            cur = cur.children[i]
        cur.end = True

    def search(self, s):
        cur = self.root
        for i in s:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.end

    def autocomplete(self, s):
        cur = self.root
        for i in s:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        words = []

        def recur(cur, s):
            if cur.end:
                words.append(s)
            for i, node in cur.children.items():
                recur(node, s+i)
        recur(cur, s)
        return words
