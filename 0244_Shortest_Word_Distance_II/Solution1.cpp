#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class WordDistance {
    unordered_map<string, vector<int>> mp;
public:
    WordDistance(vector<string>& words) {
        for (int i = 0; i < words.size(); i++) {
            mp[words[i]].push_back(i);
        }
    }

    int shortest(string word1, string word2) {
        int dis = INT_MAX;
        for (int i : mp[word1]) {
            for (int j : mp[word2])
            dis = min(dis, abs(i - j));
        }
        return dis;
    }
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(words);
 * int param_1 = obj->shortest(word1,word2);
 */

void test(string test_name, vector<string> words, string word1, string word2, int expected)
{
    WordDistance *obj = new WordDistance(words);
    int res = obj->shortest(word1, word2);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }

}

int main()
{
    vector<string> words = {"practice", "makes", "perfect", "coding", "makes"};

    string word11 = "coding";
    string word21 = "practice";
    int expected1 = 3;
    test("test1", words, word11, word21, expected1);

    string word12 = "makes";
    string word22 = "coding";
    int expected2 = 1;
    test("test2", words, word12, word22, expected2);

    return 0;
}
