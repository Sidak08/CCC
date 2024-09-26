#include <iostream>
#include <string>
#include <algorithm> // For std::sort
#define ll long long

using namespace std;

void panidrome(string str) {
    cout << str <<'\n';
    ll len = str.size();
    string corStr(len, ' ');
    for (ll i = 0; i < len - 1 ; i+= 2) {
        if (str[i] == str[i + 1]){
            corStr[i] = str[i];
            corStr[len - i] = str[i];
        } else if (!(len % 2 != 0 && ((i - 1) != (len / 2) + 1))){
            cout << "NO SOLUTION";
        }
    }
    cout << corStr;
}

int main() {
    string myString;
    getline(cin, myString);
    sort(myString.begin(), myString.end());
    panidrome(myString);
    return 0;
}


// 10100
// 1110
