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

    int t;
    cin>>t;
    
    while(t--){
        int sum=0;
        int n; cin >> n;
        for(int i = 1; i>0; i--){
            int tmp = n%10;
            sum +=tmp;
            int tmp2 = n/10;
            sum +=tmp2;
        }
        cout << sum << endl;
    }

    
    return 0;
}