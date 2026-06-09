#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const ll MAX = 2e5;
const ll INF = 1e18;
ll n,a[MAX],c[MAX],b[MAX],_a[MAX],_c[MAX];
string s;
bool solve(char** argv){
    ifstream inp(argv[1]);
    inp>>n;
    inp>>s;
    for (ll i=0; i<n; ++i) inp>>a[i];
    for (ll i=0; i<n; ++i) inp>>c[i];
    s+="0";
    ll cs=0,mx=-INF;
    for (ll i=0; i<n; ++i){
        if (s[i]=='0'){
            a[i]=c[i]-cs;
            ll cs1=cs;
            for (ll j=i+1; j<n; ++j){
                if (s[j]=='0') break;
                a[i]=min(a[i],c[j]-a[j]-cs1);
                cs1+=a[j];
            }
        }
        cs+=a[i];
        mx=max(mx,cs);
        if (mx!=c[i]){
            return 0;
        }
    }
    return 1;
}
int main(int argc, char** argv) {
    // ifstream inp(argv[1]);
    ifstream out(argv[2]);
    // ifstream ans(argv[3]);

    // return 0 = AC
    // return 1 = WA
    // return 7 = PARTIAL

    bool d=solve(argv);
    if (!d){
        string i;
        out>>i;
        cerr<<"ket qua khong ton tai, in ra -1";
        return(0?stoll(i)==-1:1);
    }else{
        for (ll i=0; i<n; ++i) out>>_a[i];
        b[0]=_a[0]; _c[0]=_a[0];
        for (ll i=1; i<n; ++i) b[i]=b[i-1]+_a[i];
        for (ll i=1; i<n; ++i) _c[i]=max(_c[i-1],b[i]);
        for (ll i=0; i<n; ++i){
            if (s[i]=='0') continue;
            if (a[i]!=_a[i]){
                cerr<<"day a khong khop";
                return 1;
            }
        }
        for (ll i=0; i<n; ++i){
            if (c[i]!=_c[i]){
                cerr<<"day c khong khop";
                return 1;
            }
        }
        cerr<<"day a hop le";
        return 0;
    }
}