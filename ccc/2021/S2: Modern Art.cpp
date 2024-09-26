#include <iostream>
#include <vector>
using namespace std;
#define lo long
#include <algorithm> // For std::transform

template <typename T>
void printVector(const std::vector<T> &vec)
{
    std::cout << "Vector elements are:" << std::endl;
    for (const T &element : vec)
    {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    lo m, n, k, goldCount = 0;

    cin >> m >> n >> k;

    std::vector<bool> matrix(m * n, false);
    for (lo i = 0; i < k; i++)
    {
        char opp;
        lo num;
        cin >> opp >> num;

        switch (opp)
        {
        case 'C':
            for (lo i = num - 1; i < n * m; i += n)
            {
                if (matrix[i] == false)
                {
                    matrix[i] = true;
                    goldCount += 1;
                }
                else
                {
                    matrix[i] = false;
                    goldCount -= 1;
                }
            }
            break;

        case 'R':
            for (lo i = (num - 1) * n; i < num * n; i++)
            {
                if (matrix[i] == false)
                {
                    matrix[i] = true;
                    goldCount += 1;
                }
                else
                {
                    matrix[i] = false;
                    goldCount -= 1;
                }
            }
            break;
        }
    }
    cout << goldCount;
}

// [
//     000000
//     000000
//     000000
//     000000
// ]

// c = 5 r = 5