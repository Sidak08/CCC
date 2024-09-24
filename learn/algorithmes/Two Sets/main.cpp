#include <iostream>
#include <string>
using namespace std;
#define ll long long


void calcSet (ll num) {
    if (num % 2 == 0) {
        if ((num / 2) % 2 == 0){
        cout << num / 2 << "\n";
        for (ll i = 0; i < num / 2; i+=2) {
            cout << num - i << " ";
            cout << i + 1 << " ";
        }
        cout << "\n" << num / 2 << "\n";
        for (ll i = 1; i < num / 2; i+=2) {
            cout << num - i << " ";
            cout << i + 1 << " ";
        }
        }
        else {
            cout << "NO";
        }
    }
    else if (((num * (num + 1)) / 2) % 2 == 0){
        ll dsVal = (num * (num + 1)) / 4;
        string sVal = "";
        string uVal = "";
        for (ll i = num; i > 0; i--){
            if (i <= dsVal){
                dsVal -= i;
                uVal += to_string(i) + " ";
            } else {
                if (!(i == 0)) {
                    sVal += to_string(i) + " ";
                }
            }
        }
        cout << "YES" << "\n" << uVal.size() / 2 << "\n" << uVal << "\n" << sVal.size() / 2 << "\n" << sVal;

    }
    else {
         cout << "NO";
    }
}
int main () {
    ll num;
    cin >> num;
    calcSet(num);
    return 0;
}
