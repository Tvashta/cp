#include <bits/stdc++.h>
using namespace std;
template <typename T>
struct Tree
{
    Tree(const T &v) : value(v), left(nullptr), right(nullptr) {}
    T value;
    Tree *left;
    Tree *right;
};

int kthSmallestInBST(Tree<int> *t, int k)
{
    static int c = 0;
    if (!t)
        return -1;
    int x = kthSmallestInBST(t->left, k);
    c += 1;
    if (c == k)
        return t->value;
    int y = kthSmallestInBST(t->right, k);
    if (x != -1)
        return x;
    if (y != -1)
        return y;
    return -1;
}