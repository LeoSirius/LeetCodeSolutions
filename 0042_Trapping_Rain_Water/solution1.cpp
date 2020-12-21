#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty())
            return 0;
        int max_l = height[0], max_r = height.back();
        int l = 0, r = height.size() - 1;
        int res = 0;
        while (l < r) {
            if (height[l] <= height[r]) {
                ++l;
                if (max_l < height[l])
                     max_l = height[l];
                else
                    res += max_l - height[l];
            } else {
                --r;
                if (max_r < height[r])
                    max_r = height[r];
                else
                    res += max_r - height[r];
            }
        }
        return res;
    }
};

void test(string test_name, vector<int> &height, int expected)
{
    int res = Solution().trap(height);
    cout << "res = " << res << endl;
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> height1 = {0,1,0,2,1,0,1,3,2,1,2,1};
    int expected1 = 6;
    test("test1", height1, expected1);

    return 0;
}
