#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> fac(n+1, 1);
        for (int i = 1; i <= n; i++)
            fac[i] = i * fac[i-1];        // fac[i] store i!

        vector<char> num_char(n, '0');
        for (int i = 0; i < n; i++)
            num_char[i] = i + 1 + '0';    // from 1 to n 的字符，存在0-n-1的索引中

        string res = "";
        k--;            // // start from 0
        for (int i = n - 1; 0 <= i; i--) {
            int idx = k / fac[i];
            k -= idx * fac[i];

            res += num_char[idx];
            num_char.erase(num_char.begin() + idx);
        }
        return res;
    }
};

void test(string test_name, int n, int k, string expected)
{
    string res = Solution().getPermutation(n, k);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 3;
    int k1 = 3;
    string expected1 = "213";
    test("test1", n1, k1, expected1);

    int n2 = 4;
    int k2 = 9;
    string expected2 = "2314";
    test("test2", n2, k2, expected2);

    int n3 = 4;
    int k3 = 15;
    string expected3 = "3214";
    test("test3", n3, k3, expected3);

    return 0;
}

// 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

// 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

// "123"
// "132"
// "213"
// "231"
// "312"
// "321"
// 给定 n 和 k，返回第 k 个排列。

// 说明：

// 给定 n 的范围是 [1, 9]。
// 给定 k 的范围是[1,  n!]。

