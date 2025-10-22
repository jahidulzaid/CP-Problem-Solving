#include <iostream>
#include <vector>
#include <numeric>

void solve() {
    long long n, m;
    std::cin >> n >> m;

    long long min_possible_m = n;
    long long max_possible_m = n * (n + 1) / 2;

    if (m < min_possible_m || m > max_possible_m) {
        std::cout << -1 << std::endl;
        return;
    }

    if (n == 1) {
        std::cout << 1 << std::endl;
        return;
    }

    long long root_k = -1;
    long long low = 1, high = n;

    while (low <= high) {
        long long mid_k = low + (high - low) / 2;
        if (mid_k == 0) {
            low = mid_k + 1;
            continue;
        }
        long long min_sum_for_k = mid_k * (mid_k + 1) / 2 + (n - mid_k);
        if (min_sum_for_k <= m) {
            root_k = mid_k;
            low = mid_k + 1;
        } else {
            high = mid_k - 1;
        }
    }

    long long k = root_k;
    long long max_sum_for_k = k * (k + 1) / 2 + (n - k) * k;

    if (m > max_sum_for_k) {
        std::cout << -1 << std::endl;
        return;
    }

    std::cout << k << std::endl;

    for (long long i = 2; i <= k; ++i) {
        std::cout << i - 1 << " " << i << std::endl;
    }

    long long num_free = n - k;
    if (num_free > 0) {
        long long sum_from_free = m - (k * (k + 1) / 2);
        long long extra_sum = sum_from_free - num_free;
        
        long long num_at_k = 0;
        if (k > 1) {
            num_at_k = extra_sum / (k - 1);
        }
        long long rem_extra = 0;
        if (k > 1) {
            rem_extra = extra_sum % (k - 1);
        }

        long long free_node_label = k + 1;
        for (long long i = 0; i < num_at_k; ++i) {
            std::cout << k << " " << free_node_label++ << std::endl;
        }

        if (rem_extra > 0) {
            std::cout << rem_extra + 1 << " " << free_node_label++ << std::endl;
        }

        while (free_node_label <= n) {
            std::cout << 1 << " " << free_node_label++ << std::endl;
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}