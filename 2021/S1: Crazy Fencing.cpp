#include <iostream>
#include <string>
#include <vector>
using namespace std;

// does not work with problem set 7 and 8 probs rounding error
int main()
{
    int num;
    cin >> num;
    vector<double> heights(num + 1);
    vector<double> widths(num);
    double sum = 0;

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
