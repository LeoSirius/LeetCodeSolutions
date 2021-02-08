#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> stk;
        int p1 = 0, p2 = 0;
        while (p1 < pushed.size() && p2 < popped.size()) {
            stk.push(pushed[p1++]);
            while (!stk.empty() && popped[p2] == stk.top()) {
                stk.pop();
                p2++;
            }
        }
        return p2 == popped.size();
    }
};

void test(string test_name, vector<int>& pushed, vector<int>& popped, bool expected)
{
    bool res = Solution().validateStackSequences(pushed, popped);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> pushed1 = {1,2,3,4,5};
    vector<int> popped1 = {4,5,3,2,1};
    bool expected1 = true;
    test("test1", pushed1, popped1, expected1);

    vector<int> pushed2 = {1,2,3,4,5};
    vector<int> popped2 = {4,3,5,1,2};
    bool expected2 = false;
    test("test2", pushed2, popped2, expected2);

    return 0;
}

// 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
// 假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 
// 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

//  

// 示例 1：

// 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
// 输出：true
// 解释：我们可以按以下顺序执行：
// push(1), push(2), push(3), push(4), pop() -> 4,
// push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1



// 示例 2：
// 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
// 输出：false
// 解释：1 不能在 2 之前弹出。
//  

// 提示：

// 0 <= pushed.length == popped.length <= 1000
// 0 <= pushed[i], popped[i] < 1000
// pushed 是 popped 的排列。


