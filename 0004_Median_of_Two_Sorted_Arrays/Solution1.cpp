#include <iostream>
#include <vector>
using namespace std;

class Solution {
    double findKth(vector<int>& nums1, vector<int>& nums2, int k)
    {
        if (!nums1.size()) return nums2[k-1];
        if (!nums2.size()) return nums1[k-1];

        int m1 = nums1.size() / 2;
        int m2 = nums2.size() / 2;
        int v1 = nums1[m1], v2 = nums2[m2];

        // 注意抛弃的时候是包括了切分索引的，
        if ((k-1) > (m1 + m2)) {
            // k在后半部分，抛弃前半部分，谁的中间值小就抛弃谁。抛弃的部分包括中间元素
            // v1 < v2 则抛弃nums1的前半部分，否则抛弃nums2的前半部分
            if (v1 < v2) {
                vector<int> nums1_second(nums1.begin() + m1 + 1, nums1.end());
                return findKth(nums1_second, nums2, k-(m1+1));
            } else {
                vector<int> nums2_second(nums2.begin() + m2 + 1, nums2.end());
                return findKth(nums1, nums2_second, k-(m2+1));
            }
        } else{
            // k在前半部分，抛弃nums1或nums2的后半部分。谁的中间值大就抛弃谁
            if (v1 < v2) {
                vector<int> nums2_first(nums2.begin(), nums2.begin() + m2);
                return findKth(nums1, nums2_first, k);
            } else {
                vector<int> nums1_first(nums1.begin(), nums1.begin() + m1);
                return findKth(nums1_first, nums2, k);
            }
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // k和这里的left，right都不是索引，而是从1开始的个数
        // 如果是基数，如5，则left = right = 3
        // 如果是偶数，如6，则left = 3, right = 4
        int left = (nums1.size() + nums2.size() + 1) / 2;
        int right = (nums1.size() + nums2.size() + 2) / 2;
        return (findKth(nums1, nums2, left) + findKth(nums1, nums2, right)) / 2;
    }
};

void test(string test_name, vector<int>& nums1, vector<int>& nums2, double expected)
{
    double res = Solution().findMedianSortedArrays(nums1, nums2);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl; 
    }
}

int main()
{
    vector<int> nums11 = {1,3};
    vector<int> nums21 = {2};
    double expected1 = 2.0;
    test("test1", nums11, nums21, expected1);

    vector<int> nums12 = {1,2};
    vector<int> nums22 = {3,4};
    double expected2 = 2.5;
    test("test2", nums12, nums22, expected2);

    return 0;
}
