#include <iostream>
#include <string>
#include <algorithm> // For std::sort
#define ll long long

using namespace std;

void panidrome(string str) {
    // cout << str <<'\n';
    ll len = str.size();
    string corStr(len, ' ');
    ll counter = 0;
    for (ll i = 0; i < len; i+=2) {
        if (str[i] == str[i + 1]){
            corStr[counter] = str[i];
            corStr[len - counter - 1] = str[i];
        } else if (!(len % 2 != 0 && ((i - 1) != (len / 2) + 1))){
            cout << "NO SOLUTION";
            return;
        } else {
            corStr[i] = str[i];
        }
        cout << str << " " << corStr << " " << i << " " << corStr[counter] << " " << corStr[len - counter] << "\n";
        counter++;
    }
    cout << corStr;
}

int main() {
    string myString;
    // getline(cin, myString);
    myString = "AAAACACBA";
    sort(myString.begin(), myString.end());
    panidrome(myString);
    return 0;
}


// 10100
// 1110
