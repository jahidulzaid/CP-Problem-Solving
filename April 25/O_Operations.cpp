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
    int t; cin >> t;
    
    while(t--){
        set<double> set;
        int a, b; 
        cin >> a >> b;
        set.insert(a + b);
        set.insert(a - b);
        set.insert(b - a);
        set.insert(a * b);
        if( a != 0){
            set.insert(double(b)/a);
        }
        if( b != 0){
            set.insert(double(a)/b);
        }
        cout << set.size() << endl;
    }    

    return 0;
}