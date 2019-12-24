#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> fac(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            fac[i] = i * fac[i-1];
        }

        vector<char> num_char(n, '0');
        for (int i = 0; i < n; i++) {
            num_char[i] = i + 1 + '0';
        }
        string res = "";
        k--;    // start from 0
        for (int i = n-1; i >= 0; i--) {
            int index = k / fac[i];
            res += num_char[index];
            num_char.erase(num_char.begin() + index);
            k -= index * fac[i];
        }
        return res;
    }
};

void test(string test_name, int n, int k, string expected)
{
    Solution s;
    if (s.getPermutation(n, k) == expected) {
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
