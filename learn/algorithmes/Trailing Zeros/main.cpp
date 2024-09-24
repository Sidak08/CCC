#include <iostream>
#define ll long long
using namespace std;

void calc(ll num) {
    ll sum = 0;
    ll currVal = 5;
    while (currVal <= num) {
        sum += num/currVal;
        currVal *= 5;
    }
    cout << sum;
}

int main () {
    ll num;
    cin >> num;
    calc(num);
    return 0;
}
