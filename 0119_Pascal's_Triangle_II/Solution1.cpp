#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex + 1, 0);
        for (int i = 0; i <= rowIndex; i++) {
            for (int j = i; j >= 0; j--) {
                if (j == 0 || j == i) {
                    res[j] = 1;
                } else {
                    res[j] = res[j] + res[j-1];
                }
            }
        }
        return res;
    }
};

void test(string test_name, int rowIndex, vector<int> expected)
{
    Solution s;
    if (s.getRow(rowIndex) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int rowIndex1 = 3;
    vector<int> expected1 = {1,3,3,1};
    test("test1", rowIndex1, expected1);

    return 0;
}
