#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int num;
    cin >> num;
    vector<long double> heights(num + 1);
    vector<long double> widths(num);
    long double sum = 0;

    for (int i = 0; i < num + 1; i++)
    {
        cin >> heights[i];
    }

    for (int i = 0; i < num; i++)
    {
        cin >> widths[i];
    }

    for (int i = 0; i < num; i++)
    {
        sum += ((heights[i] + heights[i + 1]) / 2) * widths[i];
    }

    cout << sum;
}
