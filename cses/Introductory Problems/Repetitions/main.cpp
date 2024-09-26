#include <iostream>
#include <string>
using namespace std;

void findRep(string inpStr) {
    int longestCount = 0;
    int firstPointer = 0;

    for (int i = 1; i < inpStr.size(); i++) {
        if (inpStr[i] != inpStr[firstPointer]) {
            longestCount = max(longestCount, i - firstPointer);
            firstPointer = i;
        }
    }
    // Check the last segment
    longestCount = max(longestCount, (int)inpStr.size() - firstPointer);

    cout << longestCount << endl;
}

int main() {
    string inpStr;
    cin >> inpStr;
    findRep(inpStr);
    return 0;
}
