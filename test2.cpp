#include<bits/stdc++.h>

// #include <windows.h>
// #include <psapi.h>
// size_t getMemoryUsage() {
//     PROCESS_MEMORY_COUNTERS_EX pmc;
//     GetProcessMemoryInfo(
//         GetCurrentProcess(),
//         (PROCESS_MEMORY_COUNTERS*)&pmc,
//         sizeof(pmc)
//     );
//     return pmc.PrivateUsage;
// }

using namespace std;
using ll=long long;
const ll MAX = 500;
const ll MOD = 1e9+7;
const ll INF = 500;
ll n,a[MAX],c[MAX];
map<ll,ll> lo;
void solve(){
    cin>>n;
    for (ll i=0; i<n; ++i)cin>>a[i];
    for (ll i=0; i<n; ++i){
        set<ll> t;
        for (ll j=i; j>=0; --j){
            t.insert(a[j]);
            c[i]+=t.size();
        }
    }
    for (ll i=0; i<n; ++i)cout<<c[i]<<' ';
    cout<<'\n';
}
int main(){
    auto start=chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);
    if (fopen("a.inp","r")){
        freopen("a.inp","r",stdin);
        freopen("a.out","w",stdout);
    }
    ll t=1;
    // cin>>t;
    while (t--) solve();

    auto end=chrono::high_resolution_clock::now();
    cerr<<fixed<<setprecision(6)<<"Time elapsed : "<<(chrono::duration<double>(end-start).count())<<"s"<<'\n';
    // cerr<<fixed<<setprecision(6)<<"Memory Usage : "<<getMemoryUsage()/1024.0/1024.0<<"MB"<<'\n';
    return 0;
}
