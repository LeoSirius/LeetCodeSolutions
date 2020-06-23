#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string minNumber(vector<int>& nums) {
        vector<string> strs;
        string res;
        for(auto num:nums)
            strs.push_back(to_string(num));
        sort(strs.begin(),strs.end(),compare);
        for(auto str:strs)
            res+=str;
        return res;
    }
private:
    // 按这个排序后，如第二个例子会变成30，3，34，5，9
    static bool compare(const string &a,const string &b)
    {
        // ab拼起来小于ba拼起来
        return a+b<b+a;
    }
};

void test(string test_name, vector<int>& nums, string expected)
{
    string res = Solution().minNumber(nums);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {10, 2};
    string expected1 = "102";
    test("test1", nums1, expected1);

    vector<int> nums2 = {3, 30, 34, 5, 9};
    string expected2 = "3033456";
    test("test2", nums2, expected2);

    return 0;
}


// 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

// 示例 1:
// 输入: [10,2]
// 输出: "102"

// 示例 2:
// 输入: [3,30,34,5,9]
// 输出: "3033459"

// 提示:
// 0 < nums.length <= 100

// 说明:
// 输出结果可能非常大，所以你需要返回一个字符串而不是整数
// 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
