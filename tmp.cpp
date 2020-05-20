#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<double> twoSum(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= 6; j++) {

            }
        }
    }
};

// class Solution {
// public:
//     vector<double> twoSum(int n) {
//         int dp[15][70];
//         memset(dp, 0, sizeof(dp));
//         for (int i = 1; i <= 6; i ++) {
//             dp[1][i] = 1;
//         }
//         for (int i = 2; i <= n; i ++) {
//             for (int j = i; j <= 6*i; j ++) {
//                 for (int cur = 1; cur <= 6; cur ++) {
//                     if (j - cur <= 0) {
//                         break;
//                     }
//                     dp[i][j] += dp[i-1][j-cur];
//                 }
//             }
//         }
//         int all = pow(6, n);
//         vector<double> ret;
//         for (int i = n; i <= 6 * n; i ++) {
//             ret.push_back(dp[n][i] * 1.0 / all);
//         }
//         return ret;
//     }
// }; 




// 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

// 你需要用一个浮点数数组返回答案，
// 其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

// 示例 1:
// 输入: 1
// 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

// 示例 2:
// 输入: 2
// 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
//  

// 限制：
// 1 <= n <= 11
