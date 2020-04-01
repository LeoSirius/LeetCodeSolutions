#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int depth = 0;
        vector<int> res;
        for (int i = 0; seq[i]; i++) {
            if (seq[i] == '(') {
                ++depth;
                res.push_back(depth % 2);
            } else {
                res.push_back(depth % 2);
                --depth;
            }
        }
        for (auto item : res) cout << item << " ";
        cout << endl;
        return res;
    }
};

void test(string test_name, string seq, vector<int> expected)
{
    vector<int> res = Solution().maxDepthAfterSplit(seq);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string seq1 = "(()())";
    vector<int> expected1 = {0, 1, 1, 1, 1, 0};
    test("test1", seq1, expected1);

    string seq2 = "()(())()";
    vector<int> expected2 = {0,0,0,1,1,0,1,1};
    test("test2", seq2, expected2);

    return 0;
}

// class Solution {
// public:
//     vector<int> maxDepthAfterSplit(string seq) {
//         int d = 0;
//         vector<int> ans;
//         for (char& c : seq)
//             if (c == '(') {
//                 ++d;
//                 ans.push_back(d % 2);
//             }
//             else {
//                 ans.push_back(d % 2);
//                 --d;
//             }
//         return ans;
//     }
// };

// 维护一个栈 s，从左至右遍历括号字符串中的每一个字符：

// 如果当前字符是 (，就把 ( 压入栈中，此时这个 ( 的嵌套深度为栈的高度；

// 如果当前字符是 )，此时这个 ) 的嵌套深度为栈的高度，随后再从栈中弹出一个 (。

// 下面给出了括号序列 (()(())()) 在每一个字符处的嵌套深度：

// 括号序列   ( ( ) ( ( ) ) ( ) )
// 下标编号   0 1 2 3 4 5 6 7 8 9
// 嵌套深度   1 2 2 2 3 3 2 2 2 1 
// 知道如何计算嵌套深度，问题就很简单了：只要在遍历过程中，
// 我们保证栈内一半的括号属于序列 A，一半的括号属于序列 B，那么就能保证拆分后最大的嵌套深度最小，
// 是当前最大嵌套深度的一半。要实现这样的对半分配，我们只需要把奇数层的 ( 
// 分配给 A，偶数层的 ( 分配给 B 即可。对于上面的例子，我们将嵌套深度为 1 和 3 的所有括号 (()) 
// 分配给 A，嵌套深度为 2 的所有括号 ()()() 分配给 B。


// Split the string into two sets of characters like this:

// Example 1:

//     ( ( ) ( ) )                 "(()())"

//   [ 0 1 1 1 1 0 ]

// A:  (         )                 "()"
// B:    ( ) ( )                   "()()"

// Example 2:

//     ( ) ( ( ) ) ( )             "()(())()"

//   [ 0 0 0 1 1 0 1 1 ]

// A:  ( ) (     )                 "()()"
// B:        ( )   ( )             "()()"
// The goal is to minimize the nesting depth of the parentheses in A and B, 
// where A and B are implicitly constructed from the 1s and 0s you return.


// Input: seq = "(()())"
// Output: [0,1,1,1,1,0]
// Example 2:

// Input: seq = "()(())()"
// Output: [0,0,0,1,1,0,1,1]




// A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

// It is the empty string, or
// It can be written as AB (A concatenated with B), where A and B are VPS's', or
// It can be written as (A), where A is a VPS.
// We can similarly define the nesting depth depth(S) of any VPS S as follows:

// depth("") = 0
// depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's'
// depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
// For example,  "", "()()", and "()(()())" are VPS's' (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's'.

//  

// Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's' (and A.length + B.length = seq.length).

// Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

// Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

//  

// Example 1:

// Input: seq = "(()())"
// Output: [0,1,1,1,1,0]
// Example 2:

// Input: seq = "()(())()"
// Output: [0,0,0,1,1,0,1,1]
//  

// Constraints:

// 1 <= seq.size <= 10000

