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



// Problem logic goes here
void solve() {

        string s;
        cin >> s;
        vector<int> cnt(10, 0);
        for (char c : s) {
            cnt[c - '0']++;
        }

        string ans = "";

        for (int i = 0; i < 10; ++i) {
            int n = 9 - i;
            for (int d = n; d <= 9; ++d) {
                if (cnt[d] > 0) {
                    ans += (char)(d + '0');
                    cnt[d]--;
                    break;
                }
            }
        }

        cout << ans << endl;;
}

// Main function
int main() {
    FAST_IO;
    int T = 1;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
