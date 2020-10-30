#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    int gcd(int a, int b) {
        if (b > a)
            swap(a, b);
        int r = a % b;
        while (r) {
            a = b;
            b = r;
            r = a % b;
        }
        return b;
    }
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        int num_cnt[10000] = {0};
        for (auto num : deck)
            ++num_cnt[num];

        int g = num_cnt[deck[0]];
        for (int i = 0; i < 10000; ++i) {
            if (num_cnt[i]) {
                g = gcd(g, num_cnt[i]);
                if (g < 2)
                    return false;
            }
        }
        return g >= 2;
    }
};

void test(string test_name, vector<int>& deck, bool expected)
{
    bool res = Solution().hasGroupsSizeX(deck);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> deck1 = {1,2,3,4,4,3,2,1};
    bool expected1 = true;
    test("test1", deck1, expected1);

    vector<int> deck2 = {1,1,1,2,2,2,3,3};
    bool expected2 = false;
    test("test2", deck2, expected2);

    vector<int> deck3 = {1};
    bool expected3 = false;
    test("test3", deck3, expected3);

    vector<int> deck4 = {1,1};
    bool expected4 = true;
    test("test4", deck4, expected4);

    vector<int> deck5 = {1,1,2,2,2,2};
    bool expected5 = true;
    test("test5", deck5, expected5);

    return 0;
}
