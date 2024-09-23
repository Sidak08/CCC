#include <iostream>
#include <vector>
#define ll long long
using namespace std;

void calcNum(ll row, ll col) {
    if ( row > col ) {
        ll diagnoalNum = (row * row) - (row - 1);
        if (row % 2 == 0) {
            cout << diagnoalNum + (row - col) << "\n";
        } else {
            cout << diagnoalNum - (row - col) << "\n";
        }
    } else {
        ll diagnoalNum = (col * col) - (col - 1);
        if (col % 2 == 0) {
            cout << diagnoalNum - (row - col) << "\n";
        } else {
            cout << diagnoalNum + (row - col) << "\n";
        }
    }
}

int main () {
    ll num;
    cin >> num;
    for (ll i = 0; i < num; i ++){
        ll row, col;
        cin >> row >> col;
        calcNum(row, col);
    }
    return 0;

}
