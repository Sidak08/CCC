#include <iostream>
#include <bitset>
#include <cmath>
#define ll long long

using namespace std;

void thing(ll number, bitset<16> bits){
    for (ll i = 0; i < number; i++){
        cout << bits << "\n";
        bits = bitset<16>(bits.to_ulong() + 1);
    }

}

int main() {
    ll num;
    cin >> num;
    bitset<16> bits;
    thing(pow(2, num), bits);
    return 0;
}
