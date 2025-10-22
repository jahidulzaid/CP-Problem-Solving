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

// int mxN = 1e4 + 9;
// vector<bool> is_prime(mxN, 1);


bool is_prime(int n) {
    if (n == 1)
        return true;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0)
            return false;
    }
    return true;
}



// void hi(){
//     is_prime[1] = true; 
//     is_prime[0] = false;
//     for (int i = 2; i * i < mxN; i++) {
//         if (is_prime[i]) {
//             for (int j = 2 * i; j < mxN; j += i)
//                 is_prime[j] = false;
//         }
//     }

//     // for (int i = 1; i < 100; ++i) {
//     //     cout << i << " --> " << is_prime[i] << '\n';
//     // }
// }


int main() {
    string word;
    // hi();
    while (cin >> word) {
        int total = 0;
        for (char c : word) {
            if (c >= 'a' && c <= 'z')
                total += c - 'a' + 1;
            else
                total += c - 'A' + 27;
        }

        // cout << total << '\n';

        if (is_prime(total))
            cout << "It is a prime word.\n";
        else
            cout << "It is not a prime word.\n";
    }
    return 0;
}
