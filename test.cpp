#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

const int64 NEG = -(1LL<<60);

struct FenwickMax {
    int n;
    vector<int64> bit;
    FenwickMax(int n): n(n), bit(n+1, NEG) {}

    void update(int idx, int64 val){
        for(; idx<=n; idx+=idx&-idx)
            bit[idx]=max(bit[idx],val);
    }

    int64 queryPrefix(int idx){
        int64 res=NEG;
        for(; idx>0; idx-=idx&-idx)
            res=max(res,bit[idx]);
        return res;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin>>T;

    while(T--){
        int n;
        int64 c;
        cin>>n>>c;

        vector<int64>a(n+1);

        int64 base=0;
        vector<int64> vals;

        for(int i=1;i<=n;i++){
            cin>>a[i];
            base+=a[i]-c;
            vals.push_back(a[i]);
        }

        sort(vals.begin(),vals.end());
        vals.erase(unique(vals.begin(),vals.end()),vals.end());

        int m=vals.size();

        // reverse coordinates for suffix queries
        auto revId=[&](int64 x){
            int pos=lower_bound(vals.begin(),vals.end(),x)-vals.begin()+1;
            return m-pos+1;
        };

        auto id=[&](int64 x){
            return lower_bound(vals.begin(),vals.end(),x)-vals.begin()+1;
        };

        FenwickMax suf(m), pre(m);

        vector<int64> dp(n+1,0);

        for(int i=1;i<=n;i++){
            dp[i]=dp[i-1];

            int rid=revId(a[i]);
            int64 q1=suf.queryPrefix(rid);
            if(q1!=NEG)
                dp[i]=max(dp[i],q1+c-a[i]);

            int pid=id(a[i])-1;
            if(pid>0){
                int64 q2=pre.queryPrefix(pid);
                if(q2!=NEG)
                    dp[i]=max(dp[i],q2+c);
            }

            int64 before=dp[i-1];

            suf.update(revId(a[i]),before);
            pre.update(id(a[i]),before-a[i]);
        }

        cout<<base+dp[n]<<"\n";
    }
}