#include <iostream>
#define ll long long
using namespace std;


void solv (ll num1, ll num2) {
    if (num1 >= num2) {
        ll bgT = num2 / 3;
        int r1 = num1 - (3 * bgT);
        int r2 = num2 - (3 * bgT);
        if (r1 == 1 && r2 == 2 || r1 == 2 && r2 == 1 || r1 == 0 && r2 == 0) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}
int main () {
    ll num;
    cin >> num;
    for (ll i = 0; i < num; i++){
        ll x, y;
        cin >> x >> y;
        solv(x, y);
    }
    return 0;
}
