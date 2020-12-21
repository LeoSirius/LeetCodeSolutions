#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<int> porder;
    bool is_valid_order(int s, int e)
    {
        if (e <= s) return true;
        int root_val = porder[e];
        int left_end = s;

        // 首先找到左子树的最后一个元素的索引
        for (int i = s; i < e && porder[i] < root_val; i++) {
            left_end = i;
        }
        for (int i = left_end + 1; i < e; i++) {
            if (porder[i] < root_val) {
                return false;
            }
        }
        return is_valid_order(s, left_end) && is_valid_order(left_end + 1, e - 1);
    }
public:
    bool verifyPostorder(vector<int>& postorder) {
        porder = postorder;
        return is_valid_order(0, porder.size() - 1);
    }
};

void test(string test_name, vector<int>& postorder, bool expected)
{
    bool res = Solution().verifyPostorder(postorder);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> postorder1 = {1,6,3,2,5};
    bool expected1 = false;
    test("test1", postorder1, expected1);

    vector<int> postorder2 = {1,3,2,6,5};
    bool expected2 = true;
    test("test2", postorder2, expected2);

    vector<int> postorder3 = {1,2,5,10,6,9,4,3};
    bool expected3 = false;
    test("test3", postorder3, expected3);

    return 0;
}


// 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
// 如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

// 参考以下这颗二叉搜索树：
//      5
//     / \
//    2   6
//   / \
//  1   3
// 示例 1：
// 输入: [1,6,3,2,5]
// 输出: false


// 示例 2：
// 输入: [1,3,2,6,5]
// 输出: true
 

// 提示：
// 数组长度 <= 1000