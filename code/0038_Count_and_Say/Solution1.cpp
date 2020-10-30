#include <iostream>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        if (n == 2) return "11";
        string last_say = countAndSay(n-1);
        string new_say = "";
        int count = 1;   // at least one
        for (int i = 1; last_say[i]; i++) {
            if (last_say[i] != last_say[i-1]) {
                new_say.push_back(count+'0');
                new_say.push_back(last_say[i-1]);
                count = 1;
            } else {
                count++;
            }
            if (i == last_say.size() - 1) {
                new_say.push_back(count+'0');
                new_say.push_back(last_say[i]);
            }
        }
        return new_say;
    }
};

void test(string test_name, int n, string expected)
{
    Solution s;
    string res = s.countAndSay(n);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 1;
    string expected1 = "1";
    test("test1", n1, expected1);

    int n2 = 4;
    string expected2 = "1211";
    test("test2", n2, expected2);

    int n3 = 6;
    string expected3 = "312211";
    test("test3", n3, expected3);

    return 0;
}
