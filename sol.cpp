#include<bits/stdc++.h>
using namespace std;
using ll=long long;
const ll MAX = 1e7;
const ll INF = 1e18;
ll n,a[MAX+1],dp[MAX+1];
void solve(){
    cin>>n;
    for (ll i=1; i<=n; ++i) cin>>a[i];
    dp[1]=a[1];
    for (ll i=2; i<=n; ++i) dp[i]=max(dp[i-1],dp[i-2]+a[i]);
    cout<<dp[n]<<'\n';
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);
    // freopen("sol.inp","r",stdin);
    // freopen("sol.out","w",stdout);
    ll t=1;
    // cin>>t;
    while (t--) solve();
    return 0;
}