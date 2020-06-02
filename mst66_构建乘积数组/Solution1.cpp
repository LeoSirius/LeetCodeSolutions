#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        vector<int> b(a.size(), 1);
        int cur_multiply = 1;
        for (int i = 0; i < a.size(); i++) {
            b[i] = cur_multiply;
            cur_multiply *= a[i];
        }
        cur_multiply = 1;
        for (int i = a.size() - 1; 0 <= i; i--) {
            b[i] *= cur_multiply;
            cur_multiply *= a[i];
        }
        return b;
    }
};


void test(string test_name, vector<int> a, vector<int> expected)
{
    vector<int> res = Solution().constructArr(a);
    for (auto item : res) cout << item << " ";
    cout << endl;
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> a1{1,2,3,4,5};
    vector<int> expected1{120,60,40,30,24};
    test("test1", a1, expected1);

    return 0;
}

// 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
// 其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

//  

// 示例:

// 输入: [1,2,3,4,5]
// 输出: [120,60,40,30,24]
//  

// 提示：

// 所有元素乘积之和不会溢出 32 位整数
// a.length <= 100000

