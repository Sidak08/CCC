#include <iostream>
#include <vector>
#define ll long long
using namespace std;

int main () {
    ll num;
    cin >> num;
    vector<ll> arr(num, false);

    for (ll i = 1; i < num; i++) {
        ll num;
        cin >> num;
        arr[num - 1] = true;
    }

    for (int i = 0; i < arr.size(); i++){
        if (arr[i] == false){
            cout << i + 1;
        }
    }

    return 0;
}
