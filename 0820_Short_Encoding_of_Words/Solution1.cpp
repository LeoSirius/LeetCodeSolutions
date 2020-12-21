#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        unordered_set<string> myset(words.begin(), words.end());
        for (auto word : words) {
            for (int i = 1; i < word.size(); i++) {
                myset.erase(word.substr(i));   // set.erase()如果参数没有在集合中，则什么也不做
            }
        }

        int res = 0;
        for (auto word : myset)
            res += word.size() + 1;
        return res;
    }
};

void test(string test_name, vector<string>& words, int expected)
{
    int res = Solution().minimumLengthEncoding(words);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<string> words1 = {"time", "me", "bell"};
    int expected1 = 10;
    test("test1", words1, expected1);

    return 0;
}