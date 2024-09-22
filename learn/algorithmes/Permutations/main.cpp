#include <iostream>
#include <vector>
#define ll long long
using namespace std;


void number(ll num){
    for (int i = 1; i <= num; i+= 2) {
        cout << i << " ";
    }
    for (int j = 2; j <= num; j+= 2){
         cout << j << " ";
    }
}

int main () {
    ll num;
    cin >> num;
    if (num == 1) {
        cout << 1;
    } else if (num == 4){
        cout << "2 4 1 3";
    }
    else if (num < 5) {
        cout << "NO SOLUTION";
    } else {
        number(num);
    }
    return 0;
}
