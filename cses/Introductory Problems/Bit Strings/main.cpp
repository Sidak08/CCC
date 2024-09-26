#include <iostream>
using namespace std;

const int MOD = 1000000007;

long long mod_exp(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) { // If exp is odd
            result = (result * base) % mod;
        }
        base = (base * base) % mod; // Square the base
        exp /= 2; // Divide the exponent by 2
    }
    return result;
}

int main() {
    int n;
    cin >> n;

    // Calculate 2^n % MOD
    long long result = mod_exp(2, n, MOD);
    cout << result << endl;

    return 0;
}
