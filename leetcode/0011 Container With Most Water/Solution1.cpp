#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;
        while (left <= right) {
            max_area = max(max_area, (right - left) * min(height[left], height[right]));
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        cout << "max_area = " << max_area << endl;
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

void test1()
{
    vector<int> height{1, 8, 6, 2, 5, 4, 8, 3, 7};
    test("test1", height, 49);
}

int main()
{
    test1();
    return 0;
}