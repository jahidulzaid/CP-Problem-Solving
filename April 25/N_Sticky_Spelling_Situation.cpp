// Bismillahir Rahmanir Rahim
// Jahidul Islam, Green University Of Bangladesh
#include<bits/stdc++.h>
using namespace std;

// Fast IO setup
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

// Type definitions for convenience
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

// Common macros
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define rrep(i, a, b) for (int i = (b) - 1; i >= (a); --i)
#define pn   cout << "NO\n";
#define py   cout << "YES\n";
#define mp make_pair
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front


// Function to get the K-th maximum element
int getKthMax(vector<int> v, int k) {
    sort(v.begin(), v.end(), greater<int>());
    v.erase(unique(v.begin(), v.end()), v.end());
    if (k > (int)v.size()) return INT_MIN;
    return v[k - 1];
}

bool isEven(int num) {
    return (num & 1) == 0;
}

bool isPalindrome(const string &s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    return s == rev;
}

int countDigits(int n) {
    if (n == 0) return 1;
    return floor(log10(abs(n)) + 1);
}

int sumofDigits(int n) {
    n = abs(n);
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// Problem logic goes here
void solve() {
    int n;cin>>n;
    string a, b;
    cin >> a >> b;
    // sort(a.begin(), a.end());
    // sort(b.begin(), b.end());
    // cout << a << " " << b;
    int cnt = 0;
    vector<int> freqencyA(26, 0), freqencyB(26, 0);

    for(char c:a) freqencyA[c - 'a']++;
    for(char c:b) freqencyB[c - 'a']++;

    // for(int i = 0;i<sizeof(freqencyA);i++){
    //     cout << freqencyA[i] << " ";
    // }

    for(int i =0;i<26;i++){
        if(freqencyA[i] > freqencyB[i]){
            cnt  += freqencyA[i] - freqencyB[i];
        };
        
    }
    cout << cnt << endl;
    
    

    
    }

// Main function
int main() {
    FAST_IO;
    solve();
    // int T = 1;
    // cin >> T;
    // while (T--) {
    //     solve();
    // }
    return 0;
}
