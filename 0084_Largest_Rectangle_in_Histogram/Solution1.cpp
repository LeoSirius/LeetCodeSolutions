#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        if (heights.empty())
            return 0;

        int left, right;
        int res = heights[0];
        for (int i = 0; i < heights.size(); ++i) {
            if (i > 0 && heights[i] == heights[i-1])   // 优化，不然c++此方法过不了，会超时。case heights = {1,1,1,1,,1,1.....}
                continue;
            left = right = i;
            while (0 <= left && heights[i] <= heights[left])
                --left;
            while (right < heights.size() && heights[i] <= heights[right])
                ++right;
            res = max((right - left - 1) * heights[i], res);
        }
        return res;
    }
};

void test(string test_name, vector<int>& heights, int expected)
{
    int res = Solution().largestRectangleArea(heights);
    cout << "res = " << res << endl;
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> height1 = {2,1,5,6,2,3};
    int expected1 = 10;
    test("test1", height1, expected1);

    vector<int> height2 = {};
    int expected2 = 0;
    test("test2", height2, expected2);

    return 0;
}