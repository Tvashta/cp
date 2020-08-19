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
int merge(vl a, ll l, ll m, ll h, vl t)
{
    ll inv = 0;
    ll i = l, j = m - 1, k = l;
    while ((i < m - 1) && (j <= h))
        if (a[i] <= a[j])
            t[k++] = a[i++];
        else
        {
            t[k++] = a[j++];
            inv += m - i + 1;
        }
    while (i < m - 1)
        t[k++] = a[i++];
    while (j <= h)
        t[k++] = a[j++];
    for (i = l; i <= h; i++)
        a[i] = t[i];
    return inv;
}
int mergeSort(vl a, ll l, ll h, vl t)
{
    ll inv = 0;
    if (l <= h)
    {
        ll m = (l + h) / 2;
        inv += mergeSort(a, l, m, t);
        inv += mergeSort(a, m + 1, h, t);
        inv += merge(a, l, m, h, t);
        }
    return inv;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll t, n;
    cin >> t;
    while (t--)
    {
        cin >> n;
        vl a(n);
        for (ll i = 0; i < n; i++)
            cin >> a[i];
        vl t(n, 0);
        cout << mergeSort(a, 0, n - 1, t);
        cout << endl;
    }

    return 0;
}