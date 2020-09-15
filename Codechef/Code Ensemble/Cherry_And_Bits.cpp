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
    ll n, m;
    
    cin >> n >> m;
    vector<vl> v(n, vl(m, 0));
    string s[n];
    for (ll i = 0; i < n; i++)
        cin>>s[i];
        
    for(ll i=0;i<n;i++)
        for (ll j = 0; j < m; j++)
                v[i][j]=s[i][j]-'0';
    ll q, a, b, c, d;
    cin >> q;
    vector<vl> prefix(n, vl(m, 0));
    while (q--)
        {
            cin >> a >> b >> c >> d;
            a -= 1;
            b -= 1;
            c -= 1;
            d -= 1;
            prefix[a][b] += 1;
            if (c + 1 < n && d + 1 < m)
                prefix[c + 1][d + 1] += 1;
            if (d + 1 < m)
                prefix[a][d + 1] -= 1;
            if (c + 1 < n)
                prefix[c + 1][b] -= 1;
        }
        
    for (ll i = 1; i < n; i++)
            for (ll j = 0; j < m; j++)
                prefix[i][j] += prefix[i - 1][j];

    for (ll i = 0; i < n; i++)
            for (ll j = 1; j < m; j++)
                prefix[i][j] += prefix[i][j - 1];

    for (ll i = 0; i < n; i++){
        for (ll j = 0; j < m; j++)
                if (prefix[i][j] % 2)
                    cout << !(v[i][j]);
                else
                    cout << v[i][j];
        cout<<endl;
    }
    return 0;
}