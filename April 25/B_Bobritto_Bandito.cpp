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
    optimize();

    int t;cin>>t;
    while (t--) {
        int n,m, l, r;

        cin >> n >> m >> l >> r;
        
        int a = 0, b = 0;
        if(abs(l) >= m){
            a -= m;
        }
        else{
            a = l;
            b = l + m;
        }
        cout << a << " " << b << endl;

    }

    return 0;
}