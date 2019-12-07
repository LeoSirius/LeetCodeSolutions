#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int k = m + n - 1;
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2])
                nums1[k--] = nums1[p1--];
            else
                nums1[k--] = nums2[p2--];
        }
        while (p2 >= 0) {
            nums1[k--] = nums2[p2--];
        }
    }
};

void test(string test_name, vector<int> &nums1, int m, vector<int> &nums2, int n, vector<int> expected1)
{
    Solution s;
    s.merge(nums1, m, nums2, n);
    if (nums1 == expected1) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums11 = {1,2,3,0,0,0}, nums21 = {2,5,6};
    int m1 = 3, n1 = 3;
    vector<int> expected1 = {1,2,2,3,5,6};
    test("test1", nums11, m1, nums21, n1, expected1);

    return 0;
}
