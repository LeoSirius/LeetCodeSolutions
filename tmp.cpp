#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> res;
        queue<vector<string>> paths;

        paths.push({beginWord});

        unordered_set<string> word_set;
        for (auto word : wordList)
            word_set.insert(word);

        int level = 1, min_level = INT_MAX;
        unordered_set<string> visited;
        while (!paths.empty()) {
            vector<string> path = paths.front(); paths.pop();

            if (path.size() > level) {
                for (auto word : visited)
                    word_set.erase(word);
                visited.clear();
                if (path.size() > min_level)
                    break;
                level = path.size();
                    
            }
            string last_word = path.back();
            for (int i = 0; last_word[i]; ++i) {
                string new_word = last_word;
                for (char ch = 'a'; ch <= 'z'; ++ch) {
                    new_word[i] = ch;
                    if (word_set.find(new_word) == word_set.end())
                        continue;

                    vector<string> new_path = path;
                    new_path.push_back(new_word);
                    visited.insert(new_word);
                    if (new_word == endWord) {
                        min_level = level;
                        res.push_back(new_path);
                    }
                    paths.push(new_path);
                }
            }
        }

        return res;
    }
};


void test(string test_name, string beginWord, string endWord, vector<string>& wordList, vector<vector<string>>& expected)
{
    vector<vector<string>> res = Solution().findLadders(beginWord, endWord, wordList);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string beginWord1 = "hit";
    string endWord1 = "cog";
    vector<string> wordList1 = {"hot","dot","dog","lot","log","cog"};
    vector<vector<string>> expected1 = {
        {"hit","hot","dot","dog","cog"},
        {"hit","hot","lot","log","cog"}
    };
    test("test1", beginWord1, endWord1, wordList1, expected1);

    string beginWord2 = "hit";
    string endWord2 = "cog";
    vector<string> wordList2 = {"hot","dot","dog","lot","log"};
    vector<vector<string>> expected2 = {};
    test("test2", beginWord2, endWord2, wordList2, expected2);

    return 0;
}