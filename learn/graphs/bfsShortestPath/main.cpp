#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

void printVector(const std::vector<int>& vec) {
    std::cout << "Vector elements: ";
    for (const auto& element : vec) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}

vector<int> shortestPath(vector<pair<int,int> > edges, int n, int m, int s, int t) {
    std::vector<std::vector<int> > edgeMatrix(n, std::vector<int>(n, 0)); // n x n matrix

    // Build the adjacency matrix
    for (const auto& edge : edges) {
        edgeMatrix[edge.first - 1][edge.second - 1] = 1; // Adjust for 0-indexing
        edgeMatrix[edge.second - 1][edge.first - 1] = 1; // Adjust for 0-indexing
    }

    queue<int> order;
    vector<bool> seen(n, false); // Initialize seen with false

    order.push(s - 1); // Adjust for 0-indexing
    seen[s - 1] = true; // Mark the starting node as seen

    bool found = false;

    while (!order.empty() || !found) {
        int current = order.front();
        order.pop(); // Pop the current node after processing

        cout << "Processing node: " << (current + 1) << endl; // Debug output

        for (int i = 0; i < n; i++) { // Loop through all nodes
            if (edgeMatrix[current][i] == 1 && !seen[i]) {
                order.push(i); // Push the adjacent node index
                seen[i] = true; // Mark as seen
            }
        }
    }

    vector<int> ret; // Modify to collect your path if needed
    return ret; // Currently returns an empty vector
}

int main() {
    cout << "Hello, World!" << endl;
    vector<std::pair<int, int> > vec;
    vec.push_back(std::make_pair(1, 2));
    vec.push_back(std::make_pair(2, 3));
    vec.push_back(std::make_pair(3, 4));
    vec.push_back(std::make_pair(1, 3));

    shortestPath(vec, 4, 4, 1, 4);
    return 0;
}
