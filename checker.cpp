#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const ll MAX = 1e6;
const ll INF = 1e18;
int main(int argc, char** argv) {
    ifstream inp(argv[1]);
    ifstream out(argv[2]);
    // ifstream ans(argv[3]);
    
    // return 0 = AC
    // return 1 = WA
    // return 7 = PARTIAL
    ll t;
    inp>>t;
    ll c=1;
    while (t--){
        ll p,l,d;
        inp>>p;
        out>>l>>d;
        if (l+d!=p){
            cerr<<"l+d!=p (test "<<c<<")"<<'\n';
            return 1;
        }
        ll s=sqrt(l*d);
        while (s*s>l*d)--s;
        while (s*s<l*d)++s;
        if (s*s!=l*d){
            cerr<<"l*d not chinh phuong (test "<<c<<")"<<'\n';
            return 1;
        }
        ++c;
    }
    cerr<<"all tests ok"<<'\n';
    return 0;
}