#include<bits/stdc++.h>

#include <windows.h>
#include <psapi.h>

using namespace std;
using ll=long long;
const ll MAX = 5001;
const ll INF = 1e14;

auto start=chrono::high_resolution_clock::now();

size_t getMemoryUsage() {
    PROCESS_MEMORY_COUNTERS_EX pmc;
    GetProcessMemoryInfo(
        GetCurrentProcess(),
        (PROCESS_MEMORY_COUNTERS*)&pmc,
        sizeof(pmc)
    );
    return pmc.PrivateUsage;
}

ll n,c[MAX],s[MAX],dp[MAX][MAX];
void solve(){
    cin>>n;
    for (ll i=1; i<=n; ++i) cin>>c[i];
    for (ll i=1; i<=n; ++i) cin>>s[i];
    start=chrono::high_resolution_clock::now();

    for (ll l=1; l<=n; ++l){
        for (ll i=1; i+l-1<=n; ++i){
            if (l==1) dp[i][i]=s[i];
            else{
                ll j=i+l-1;
                dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
                if (c[i]==c[j]) dp[i][j]=max(dp[i][j],dp[i+1][j-1]+s[i]+s[j]);
            }
        }
    }
    cout<<dp[1][n]<<'\n';
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("a.inp","r",stdin);
    freopen("a.out","w",stdout);
    ll t=1;
    // cin>>t;
    while (t--) solve();

    auto end=chrono::high_resolution_clock::now();
    cerr<<fixed<<setprecision(6)<<"Time elapsed : "<<(chrono::duration<double>(end-start).count())<<"s"<<'\n';
    cerr<<fixed<<setprecision(6)<<"Memory Usage : "<<getMemoryUsage()/1024.0/1024.0<<"MB"<<'\n';
    return 0;
}