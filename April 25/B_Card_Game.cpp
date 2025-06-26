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
        int a1, a2;
        int b1, b2;
        cin >> a1 >> a2 >> b1 >> b2 ;
        bool w = true;
        int ar[4] = {a1, a2, b1, b2};
        sort(ar, ar+4, greater<int>());
        int cnt = 0;
        
        // a1,a2 b1,b2
        int sun = (a1 > b1) + (a2 > b2);
        int sla = (a1 < b1) + (a2 < b2);
        if( sun > sla) cnt++;
        // a1,a2 b2,b1
        sun = (a1>b2)+(a2>b1);
        sla = (a1<b2)+(a2<b1);
        if( sun > sla) cnt++;

        // a2,a1 b1,b2
        sun = (a2>b1)+(a1>b2);
        sla = (a2<b1)+(a1<b2);
        if( sun > sla) cnt++;

        // a2,a1 b2,b1
        sun = (a2>b2)+(a1>b1);
        sla = (a2<b2)+(a1<b1);
        if( sun > sla) cnt++;
        

        cout << cnt << endl;


    }

    
    return 0;
}