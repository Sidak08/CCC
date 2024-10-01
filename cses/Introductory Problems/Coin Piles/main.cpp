#include <cmath>
#include <iostream>
#define ll long long
using namespace std;

void solvRecur(ll num1, ll num2) {
    ll big, small;
    if (num1 > num2) {
         big = num1;
        small = num2;
    } else {
        big = num2;
        small = num1;
    }
    ll x = big - small;
        x = small - x;
    if (x < 0) {
        cout << "NO" << "\n";
    } else {
        if (x % 3 == 0) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}

//

int main() {
    ll num;
    cin >> num;
    for (ll i = 0; i < num; i++) {
        ll x, y;
        cin >> x >> y;
        solvRecur(x, y);
    }
    return 0;
}
