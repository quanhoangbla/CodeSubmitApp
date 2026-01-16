#include<bits/stdc++.h>
using namespace std;
using ll = long long;
ll l,r;
bool s(ll n){
    n*=10;
    ll res=0;
    while (n/=10) res+=n%10;
    return res%2==0;
}
ll f(ll x){
    if (x&1)return (x+1)/2;
    return x/2+s(x);
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("sol.inp","r",stdin);
    freopen("sol.out","w",stdout);
    cin>>l>>r;
    cout<<f(r)-f(l-1)<<'\n';
    return 0;
}