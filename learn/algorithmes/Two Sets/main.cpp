#include <iostream>
#include <string>
using namespace std;
#define ll long long


void calcSet (ll num) {
    if (((num * (num + 1)) / 2) % 2 == 0){
        ll dsVal = (num * (num + 1)) / 4;
        string sVal = "";
        string uVal = "";
        ll sSum = 0;
        ll uSum = 0;
        for (ll i = num; i > 0; i--){
            if (i <= dsVal){
                dsVal -= i;
                uVal += to_string(i) + " ";
                uSum ++;
            } else {
                    sVal += to_string(i) + " ";
                    sSum++;
            }
        }
        cout << "YES" << "\n" << uSum << "\n" << uVal << "\n" << sSum << "\n" << sVal;
    } else {
        cout << "NO";
    }
}

int main () {
    ll num;
    cin >> num;
    calcSet(num);
    return 0;
}
