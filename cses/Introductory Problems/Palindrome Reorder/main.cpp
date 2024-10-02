#include <iostream>
#include <string>
#include <unordered_map>
#define ll long long

using namespace std;

void panidrome(unordered_map<char, ll>& alaphaSet, int len) {
double oddPair = -1;
string oddPairItem;
string corStr(len, ' ');
ll counter = 0;
 //cout << pair.first << ": " << pair.second << endl;

    for (const auto& pair : alaphaSet) {
        // cout << oddPair << "\n";
        if (pair.second % 2 != 0) {
            oddPair += 1;
            oddPairItem = pair.first;
        } else {
                for (int i = 0; i < pair.second / 2; i++){
                    corStr[counter] = pair.first;
                    corStr[len - counter - 1] = pair.first;
                    // cout << "\n" << counter << len - counter - 1;
                    counter++;
                }
            }
        }
        if (oddPair == 0) {
            for (int i = 0; i < (alaphaSet[oddPairItem[0]] + 1) / 2; i++){
                corStr[(len / 2) + i] = oddPairItem[0];
                corStr[(len / 2) - i] = oddPairItem[0];
            }
        }
        if (oddPair > 0) {
                cout << "NO SOLUTION" << "\n";
                return;
        }
     cout << corStr;
}


void genHashSet (string myStr, unordered_map<char, ll>& alaphaSet) {
    for (ll i = 0; i < myStr.size(); i++){
        alaphaSet[myStr[i]]++;
    }
    return;
}

int main() {
    string myString;
    getline(cin, myString);
    // myString = "ABABABABAB";
    unordered_map<char, ll> alaphaSet;
    genHashSet(myString, alaphaSet);
    // for (const auto& pair : alaphaSet) {
    //     cout << pair.first << ": " << pair.second << endl;
    // }
    panidrome(alaphaSet, myString.size());
    return 0;
}
