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
        vl m;
        m.pb(a[0]);
        for (ll i = 1; i < n; i++)
        {
            
            auto it = upper_bound(m.begin(), m.end(), a[i]);
            if (it-m.begin() == m.size())
                m.pb(a[i]);
            else
                m[it - m.begin()] = a[i];
        }
        cout<<m.size()<<" ";
        for (auto it : m)
            cout << it << " ";
        cout << endl;
    }

    return 0;
}