#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int res = 0;
    void merge_sort(vector<int>& nums, vector<int>& tmp, int l, int r)
    {
        if (l >= r) return;

        int mid = l + (r - l) / 2;
        merge_sort(nums, tmp, l, mid);
        merge_sort(nums, tmp, mid + 1, r);
        int pl = l, pr = mid + 1, ptmp = l;
        while (pl <= mid && pr <= r) {
            if (nums[pr] < nums[pl]) {
                 // 关键点，也是归并排序添加的唯一一行代码。
                 // 在pr比pl的小，说明是逆序。
                 // pr的放到前面后，从pl到mid的都比mid大，说明这些逆序都消除了
                res += (mid + 1 - pl);
                tmp[ptmp++] = nums[pr++];
                
            } else {
                tmp[ptmp++] = nums[pl++];
            }
        }
        if (pl <= mid) copy(nums.begin()+pl, nums.begin()+mid+1, tmp.begin()+ptmp);
        if (pr <= r) copy(nums.begin()+pr, nums.begin()+r+1, tmp.begin()+ptmp);
        copy(tmp.begin()+l, tmp.begin()+r+1, nums.begin()+l);
    }

    int reversePairs(vector<int>& nums) {
        vector<int> tmparr(nums.size(), 0);
        merge_sort(nums, tmparr, 0, nums.size() - 1);
        return res;
    }
};

void test(string test_name, vector<int>& nums, int expected)
{
    int res = Solution().reversePairs(nums);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {7,5,6,4};
    int expected1 = 5;
    test("test1", nums1, expected1);

    return 0;
}

// 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
// 输入一个数组，求出这个数组中的逆序对的总数。

// 示例 1:
// 输入: [7,5,6,4]
// 输出: 5
//  

// 限制：
// 0 <= 数组长度 <= 50000
