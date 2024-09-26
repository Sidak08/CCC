#include <iostream>
#include <vector>
#define ll long long
using namespace std;

void incArry (vector<long long> numArry) {
    long long counter = 0;
    for (long long i = 1; i < numArry.size(); i++){
        if (numArry[i] < numArry[i - 1]){
            // cout << numArry[i - 1] << " " << numArry[i] << " " <<  numArry[i - 1] - numArry[i] << "\n";
            counter += numArry[i - 1] - numArry[i];
            numArry[i] = numArry[i - 1];
        }
    }
    cout << counter;
}

int main () {
    long long num;
    cin >> num;
    vector<long long> inputArry(num);
    for (long long i = 0; i < num; i++) {
        long long num;
        cin >> num;
        inputArry[i] = num;
    }
    incArry(inputArry);
    return 0;
}
