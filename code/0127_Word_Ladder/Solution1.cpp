#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<string> que;
        que.push(beginWord);
        int res = 0;

        while (!que.empty()) {
            res++;
            int cur_border_size = que.size();
            while (cur_border_size--) {
                string hop = que.front(); que.pop();
                if (hop == endWord)
                    return res;

                // 把用过的单词标记为“”
                for (auto &word : wordList) {
                    if (word == "")
                        continue;
                    int diff_cnt = 0;    // 不同char的个数
                    for (int i = 0; i < word.size(); i++) {
                        if (word[i] != hop[i]) diff_cnt++;
                        if (1 < diff_cnt) break;
                    }
                    if (diff_cnt <= 1) {
                        que.push(word);
                        word = "";
                    }
                }
            }
        }
        return 0;
    }
};


void test(string test_name, string beginWord, string endWord, vector<string>& wordList, int expected1)
{
    int res = Solution().ladderLength(beginWord, endWord, wordList);
    if (res == expected1)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string beginWord1 = "hit";
    string endWord1 = "cog";
    vector<string> wordList1 = {
        "hot","dot","dog","lot","log","cog"
    };
    int expected1 = 5;
    test("test1", beginWord1, endWord1, wordList1, expected1);

    string beginWord2 = "hit";
    string endWord2 = "cog";
    vector<string> wordList2 = {
        "hot","dot","dog","lot","log"
    };
    int expected2 = 0;
    test("test2", beginWord2, endWord2, wordList2, expected2);

    return 0;
}

// Given two words (beginWord and endWord), and a dictionary's' word list,
//  find the length of shortest transformation sequence from beginWord to endWord,
//  such that:

// Only one letter can be changed at a time.
// Each transformed word must exist in the word list.
// Note:

// Return 0 if there is no such transformation sequence.
// All words have the same length.
// All words contain only lowercase alphabetic characters.
// You may assume no duplicates in the word list.
// You may assume beginWord and endWord are non-empty and are not the same.

// Example 1:

// Input:
// beginWord = "hit",
// endWord = "cog",
// wordList = ["hot","dot","dog","lot","log","cog"]

// Output: 5

// Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
// return its length 5.

// Example 2:

// Input:
// beginWord = "hit"
// endWord = "cog"
// wordList = ["hot","dot","dog","lot","log"]

// Output: 0

// Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

