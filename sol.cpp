#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("sol.inp","r",stdin);
    freopen("sol.out","w",stdout);
    int N;
    cin >> N;

    vector<long long> x(N);
    for (int i = 0; i < N; i++) cin >> x[i];

    if (N == 0) {
        cout << 0;
        return 0;
    }
    if (N == 1) {
        cout << x[0];
        return 0;
    }

    long long prev2 = 0;     // dp[i-2]
    long long prev1 = x[0];  // dp[i-1]

    for (int i = 1; i < N; i++) {
        long long cur = max(prev1, prev2 + x[i]);
        prev2 = prev1;
        prev1 = cur;
    }

    cout << prev1;
    return 0;
}
