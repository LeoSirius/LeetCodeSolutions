#include <iostream>
#include <vector>
using namespace std;

class Solution {
    int partition(vector<int>& nums, int l, int r)
    {
        int pivot = nums[r];
        int start = l;
        for (int i = l; i <= r; ++i) {
            if (nums[i] < pivot) {
                swap(nums[start++], nums[i]); // 比pivot小，放在前面，则start之后都是>=pivot的
            }
        }
        swap(nums[r], nums[start]);    // 最后pivot复位，start就是pivot的索引
        return start;
    }

    int randomized_partition(vector<int>& nums, int l, int r)
    {
        // r-l+1就是区间长度。这样生成的随机数在[0,len)之间，如rand() % 10结果是[0,9]
        // 最后再加l，pivot_idx即在[l,r)
        int pivot_idx = rand() % (r - l + 1) + l;
        swap(nums[r], nums[pivot_idx]);
        return partition(nums, l, r);
    }

    void randomized_quick_sort(vector<int>& nums, int l, int r)
    {
        if (l < r) {
            int pos = randomized_partition(nums, l, r);
            randomized_quick_sort(nums, l, pos - 1);
            randomized_quick_sort(nums, pos + 1, r);
        }
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        srand(unsigned(time(nullptr)));
        randomized_quick_sort(nums, 0, nums.size() - 1);
        return nums;
    }
};

void test(string test_name, vector<int> nums, vector<int> expected)
{
    vector<int> res = Solution().sortArray(nums);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {5,2,3,1};
    vector<int> expected1 = {1,2,3,5};
    test("test1", nums1, expected1);

    vector<int> nums2 = {5,1,1,2,0,0};
    vector<int> expected2 = {0,0,1,1,2,5};
    test("test2", nums2, expected2);

    return 0;
}
