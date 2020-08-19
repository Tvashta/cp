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
vl visited;
vl temp;
void dfs(vl adj[], ll i)
{
    if (visited[i] == 0)
    {
        visited[i] = 1;
        temp.pb(i);
        for (auto j : adj[i])
            if (visited[j] == 0)
                dfs(adj, j);
    }
}
bool getParity(ll n)
{
    bool parity = 0;
    while (n)
    {
        parity = !parity;
        n = n & (n - 1);
    }
    return parity;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll t, n, m;
    cin >> t;
    while (t--)
    {
        cin >> n >> m;
        vl a(n);
        for (ll i = 0; i < n; i++)
        {
            cin >> a[i];
            visited.pb(0);
        }
        vl adj[n];
        for (ll i = 0; i < m; i++)
        {
            ll u, v;
            cin >> u >> v;
            adj[u - 1].pb(v - 1);
            adj[v - 1].pb(u - 1);
        }
        ll le = 0, lo = 0;
        vl t1;
        for (ll j = 0; j < n; j++)
        {
            if (visited[j] == 0)
            {
                temp.clear();
                dfs(adj, j);
                if(temp.size()>t1.size())
                t1=temp;
                
            }
        }
        for (auto i : t1)
            if (getParity(a[i]))
                        lo += 1;
                    else
                        le += 1;

        ll q;
        cin >> q;
        bool x = getParity(a[0]);
        while (q--)
        {
            ll c, k;
            cin >> c >> k;
            ll o, e;
            if (getParity(a[0] ^ k) != x)
            {
                o = le;
                e = lo;
            }
            else
            {
                o = lo;
                e = le;
            }
            if (c == 1)
                cout << o << endl;
            else
                cout << e << endl;
        }
    }

    return 0;
}