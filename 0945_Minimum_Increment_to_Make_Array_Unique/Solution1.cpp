#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        int hash[50000] = {0};
        for (int i = 0; i < A.size(); ++i)
            ++hash[A[i]];
        int res = 0;
        for (int i = 0; i < 50000; ++i) {
            if (hash[i] > 1) {
                res += hash[i] - 1;
                hash[i+1] += hash[i] - 1;
                hash[i] = 0;
            }
        }
        return res;
    }
};

void test(string test_name, vector<int>& A, int expected)
{
    int res = Solution().minIncrementForUnique(A);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> A1 = {1,2,2};
    int expected1 = 1;
    test("test1", A1, expected1);;

    vector<int> A2 = {3,2,1,2,1,7};
    int expected2 = 6;
    test("test2", A2, expected2);

    return 0;
}
