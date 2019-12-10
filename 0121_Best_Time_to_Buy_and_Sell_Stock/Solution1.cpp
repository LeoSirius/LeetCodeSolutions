#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_cur = 0, max_sofar = 0;
        for (int i = 1; i < prices.size(); i++) {
            max_cur = max(0, max_cur += (prices[i] - prices[i-1]));
            max_sofar = max(max_sofar, max_cur);
        }
        return max_sofar;
    }
};

void test(string test_name, vector<int>& prices, int expected)
{
    Solution s;
    if (s.maxProfit(prices) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> prices1 = {7,1,5,3,6,4};
    int expected1 = 5;
    test("test1", prices1, expected1);

    vector<int> prices2 = {7,6,4,3,1};
    int expected2 = 0;
    test("test2", prices2, expected2);

    return 0;
}

// Example 1:

// Input: [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
//              Not 7-1 = 6, as selling price needs to be larger than buying price.
// Example 2:

// Input: [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.
