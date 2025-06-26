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
    string s;
    cin >> s;
    int mxlen = 1, clen = 1;

    
    for (int i = 1; i<s.length(); i++){
        if ( s[i] == s[i -1]){
            clen++;
            mxlen = max(mxlen, clen);
        }else{
            clen = 1;
        }
    }
    cout << mxlen << endl;
    return 0;
}