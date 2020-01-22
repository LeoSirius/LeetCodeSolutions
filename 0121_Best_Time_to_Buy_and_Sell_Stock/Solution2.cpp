#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1) return 0;
        int res = 0, min_price = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            res = max(res, prices[i] - min_price);
            min_price = min(min_price, prices[i]);
        }
        return res;
    }
};

void test(string test_name, vector<int> &prices, int expected)
{
    if (Solution().maxProfit(prices) == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
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
