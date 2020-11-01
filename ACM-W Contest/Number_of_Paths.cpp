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
ll c = 0;
void dfs(int i, int v[], vl a[])
{
    v[i] = 1;
    c += 1;
    for (auto j : a[i])
    {
        if (!v[j])
            dfs(j, v, a);
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll n, k;
    cin >> n >> k;
    vl a[100];
    int v[100] = {0};
    for (ll i = 0; i < k; i++)
    {
        ll u, v;
        cin >> u >> v;
        a[u - 1].pb(v - 1);
        a[v - 1].pb(u - 1);
    }
    ll m = 0;
    for (ll i = 0; i < n; i++)
    {
        if (!v[i])
        {
            c = 0;
            dfs(i, v, a);
            m += c * c - c;
        }
    }
    cout << m << endl;

    return 0;
}