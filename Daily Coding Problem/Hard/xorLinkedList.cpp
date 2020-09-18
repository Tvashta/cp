// # An XOR linked list is a more memory efficient doubly linked list.
// # Instead of each node holding next and prev fields, it holds a field named both,
// # which is an XOR of the next node and the previous node. Implement an XOR linked list
// # it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
// # If using a language that has no pointers(such as Python),
// # you can assume you have access to get_pointer and dereference_pointer functions
// # that converts between nodes and memory addresses.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<ll, ll> pl;
#define F first
#define S second
#define pb push_back
#define mp make_pair
const ll mod = 100000007;
class node
{
public:
    ll val;
    node *both;
};
class xorLL
{
public:
    node *head = NULL;
    node *tail = NULL;
    ll sz = 0;
    void add(ll x)
    {
        node *cur = new node();
        cur->val = x;
        if (head == NULL)
        {
            cur->both = NULL;
            head = cur;
        }
        else if (head == tail)
            cur->both = head;
        else
        {
            cur->both = tail;
            tail->both = (node *)((uintptr_t)tail->both ^ (uintptr_t)cur);
        }
        tail = cur;
        sz += 1;
    }
    ll get(ll x)
    {
        node *cur = new node();
        node *prev = NULL;
        cur = head;
        for (int i = 0; i < x; i++)
        {
            if (cur == NULL)
                return -1;
            prev = cur;
            cur = (node *)((uintptr_t)cur->both ^ (uintptr_t)prev);
        }
        return prev->val;
    }
};
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    return 0;
}