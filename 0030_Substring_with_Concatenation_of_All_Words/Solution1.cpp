#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        int s_len = s.size();
        int words_len = words.size();

        if (!s_len || !words_len)
            return res;

        int word_len = words[0].size();

        unordered_map<string, int> words_cnt;
        for (auto word : words)
            ++words_cnt[word];

        // words总长度 = word_len * words_len
        // 假设 s = "12345"
        // 假设 word_l * words_len = 2
        // s_len - words_len * word_l + 1 = 4，即i最后最指向4，45刚好是最后两个
        for (int i = 0; i < s_len - word_len * words_len + 1; i++) {
            unordered_map<string, int> seen;
            int j = 0;
            for (; j < words_len; j++) {
                string substr = s.substr(i + j * word_len, word_len);
                // 1.当前word在words中，但是数量超过了
                // 2.当前word不在words中
                // 上面两种情况都不符合要求
                if (words_cnt.find(substr) != words_cnt.end()) {
                    ++seen[substr];
                    if (seen[substr] > words_cnt[substr])
                        break;
                } else {
                    break;
                }
            }
            // 当所有words遍历完时，没有出现上面两种情况，则符合要求
            if (j == words_len)
                res.push_back(i);
        }
        return res;
    }
};


void test(string test_name, string s, vector<string>& words, vector<int> &expected)
{
    vector<int> res = Solution().findSubstring(s, words);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "barfoothefoobarman";
    vector<string> words1 = {"foo","bar"};
    vector<int> expected1 = {0, 9};
    test("test1", s1, words1, expected1);

    string s2 = "wordgoodgoodgoodbestword";
    vector<string> words2 = {"word","good","best","word"};
    vector<int> expected2 = {};
    test("test2", s2, words2, expected2);
    return 0;
}
