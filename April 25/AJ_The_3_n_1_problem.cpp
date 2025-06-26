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

int Clen(int n) {
    int count = 1;
    while (n != 1) {
        if (n % 2 == 0)
            n = n / 2;
        else
            n = 3 * n + 1;
        count++;
    }
    return count;
}

int main() {
    int i, j;

    while (cin >> i >> j) {
        int lo = min(i, j);
        int hg = max(i, j);
        int mxC = 0;

        for (int k = lo; k <= hg; ++k) {
            int cC = Clen(k);
            if (cC > mxC) {
                mxC = cC;
            }
        }
        cout << i << " " << j << " " << mxC << endl;
    }

    return 0;
}