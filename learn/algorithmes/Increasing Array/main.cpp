#include <iostream>
#include <vector>
#define ll long long
using namespace std;

void incArry (vector<int> numArry) {
    int counter = 0;
    for (int i = 1; i < numArry.size(); i++){
        if (numArry[i] < numArry[i - 1]){
            counter -= numArry[i] - numArry[i - 1];
        }
    }
    cout << counter;
}

int main () {
    int num;
    cin >> num;
    vector<int> inputArry(num);
    for (int i = 0; i < num; i++) {
        int num;
        cin >> num;
        inputArry[i] = num;
    }
    incArry(inputArry);
    return 0;
}
