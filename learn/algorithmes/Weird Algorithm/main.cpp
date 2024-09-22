#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

long long recursive(long long number){
    cout << number << " ";
    if (number == 1) {
        return number;
    }
    else if (number % 2 == 0){
        return recursive(number / 2);
    } else {
        return recursive((number * 3) + 1);
    }
}

int main () {
    long long number;
    cin >> number;
    recursive(number);
    return 0;
}
