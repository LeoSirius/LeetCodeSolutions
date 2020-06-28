#include <iostream>
using namespace std;

class Trie {
    // 这里需要给个初始值，不然会报错
    bool is_end = false;
    Trie* next[26] = {nullptr};
public:
    /** Initialize your data structure here. */
    Trie() {
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* node = this;
        for (char ch : word) {
            if (node->next[ch - 'a'] == nullptr) {
                node->next[ch - 'a'] = new Trie();
            }
            node = node->next[ch - 'a'];
        }
        node->is_end = true;
    }

    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* node = this;
        for (auto ch : word) {
            node = node->next[ch - 'a'];
            if (!node) return false;
        }
        return node->is_end;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Trie* node = this;
        for (auto ch : prefix) {
            node = node->next[ch - 'a'];
            if (!node) return false;
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

// Implement a trie with insert, search, and startsWith methods.

// Example:

// Trie trie = new Trie();

// trie.insert("apple");
// trie.search("apple");   // returns true
// trie.search("app");     // returns false
// trie.startsWith("app"); // returns true
// trie.insert("app");   
// trie.search("app");     // returns true
// Note:

// You may assume that all inputs are consist of lowercase letters a-z.
// All inputs are guaranteed to be non-empty strings.

void test1()
{
    Trie *trie = new Trie();
    trie->insert("apple");
    bool res1 = trie->search("apple");   // true
    bool res2 = trie->search("app");     // false
    bool res3 = trie->startsWith("app"); // true
    trie->insert("app");
    bool res4 = trie->search("app");     // true
    if (res1 == true && res2 == false && res3 == true && res4 == true)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

int main()
{
    test1();
    return 0;
}

