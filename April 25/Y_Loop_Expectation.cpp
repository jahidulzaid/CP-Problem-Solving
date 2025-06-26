// Bismillahir Rahmanir Rahim
// Jahidul Islam, Green University Of Bangladesh
// 

#include <bits/stdc++.h>
using namespace std;
#define optimize() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define endl '\n'
#define tt long long t; cin >> t; 
#define ll long long
#define pb push_back

#ifdef LOCAL
#include "debug.h"
#endif

// #ifdef ONLINE_JUDGE
// #include "debug.h"
// #endif

int main() {
    int t;
    cin >> t;

    const int MAX_N = 100000;
    vector<double> a(MAX_N + 1, 0.0);


    for (int i = 1; i <= MAX_N; ++i) {
        a[i] = a[i - 1] + 1.0 / i;
    }

    while (t--) {
        int n;
        cin >> n;
        cout << fixed << setprecision(1) << a[n] << endl;
    }

    return 0;
}
