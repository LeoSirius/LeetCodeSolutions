#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_area = 0;
        int left = 0, right = height.size() - 1;
        while (left < right) {
            max_area = max(max_area, min(height[left], height[right]) * (right - left));
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max_area;
    }
};

void test(string test_name, vector<int>& height, int res)
{
    Solution s;
    if (res == s.maxArea(height)) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> height1{1, 8, 6, 2, 5, 4, 8, 3, 7};
    int expected1 = 49;
    test("test1", height1, expected1);
    return 0;
}
