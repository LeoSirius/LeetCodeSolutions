#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool verifyPostorder(vector<int>& postorder) {

    }
};

// class Solution {
// public:
//     bool verifyPostorder(vector<int>& postorder) {
//         if(postorder.empty()){
//             return true;
//         }
//         return VerifySquenceOfBST(postorder, 0, postorder.size()-1);
//     }
//     bool VerifySquenceOfBST(const vector<int>& nums, int start, int end){
//         if(start>=end){
//             return true;
//         }
//         int left = start;
//         while(left<end && nums[left]<nums[end]){
//             ++ left;
//         }
//         for(int i=left; i<end; ++i){
//             if(nums[i]<=nums[end]){
//                 return false;
//             }
//         }

//         return VerifySquenceOfBST(nums, start, left-1) &&
//                VerifySquenceOfBST(nums, left, end-1);
//     }  
// };

void test(string test_name, vector<int>& postorder, bool expected)
{
    bool res = Solution().verifyPostorder(postorder);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed";
    }
}

int main()
{
    vector<int> postorder1 = {1,6,3,2,5};
    bool expected1 = false;

    vector<int> postorder2 = {1,3,2,6,5};
    bool expected2 = true;
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