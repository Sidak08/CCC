#include <iostream>
#define ll long long
using namespace std;

void solvRecur(ll num1, ll num2) {
    while (num1 > 0 || num2 > 0) {
        if (num1 >= 2 && num2 >= 1) {
            num1 -= 2;
            num2 -= 1;
        } else if (num1 >= 1 && num2 >= 2) {
            num1 -= 1;
            num2 -= 2;
        } else {
            cout << "NO" << "\n";
            return;
        }
    }
    cout << "YES" << "\n";
}

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
