#include <iostream>
using namespace std;

class WordDictionary {
    bool is_end = false;
    WordDictionary *next[26] = {nullptr};
public:
    /** Initialize your data structure here. */
    WordDictionary() {

    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        WordDictionary *node = this;
        for (char ch : word) {
            if (node->next[ch - 'a'] == nullptr) {
                node->next[ch - 'a'] = new WordDictionary();
            }
            node = node->next[ch - 'a'];
        }
        node->is_end = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return searchWord(this, word);
    }
    bool searchWord(WordDictionary* node, string word) {
        if(word.size()==1) {  //边界
            if(isalpha(word[0])) {
                if(node->next[word[0]-'a'] && node->next[word[0]-'a']->is_end)
                    return true;
                return false;
            }
            else {
                for(int i=0; i<26; i++)
                    if(node->next[i] && node->next[i]->is_end)
                        return true;
                return false;
            }
        }
        else {
            if(isalpha(word[0])) {
                if(node->next[word[0]-'a'])
                    return searchWord(node->next[word[0]-'a'], word.substr(1, word.size()-1));
                else
                    return false;
            }
            else {
                bool b;
                for(int i=0; i<26; i++) {
                    if(node->next[i]){
                        b = searchWord(node->next[i], word.substr(1, word.size()-1));
                        if(b)   return true;
                    }
                }
                return false;
            }
        }
    }
};


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */

void test1()
{
    WordDictionary *obj = new WordDictionary();
    obj->addWord("bad");
    obj->addWord("dad");
    obj->addWord("mad");
    bool res1 = obj->search("pad");    // false
    bool res2 = obj->search("bad");    // true
    bool res3 = obj->search(".ad");    // true
    bool res4 = obj->search("b..");    // true

    if (res1 == false && res2 == true && res3 == true && res4 == true)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

void test2()
{
    WordDictionary *obj = new WordDictionary();
    obj->addWord("a");
    obj->addWord("a");
    bool res1 = obj->search(".");    // true;
    bool res2 = obj->search("a");    // true;
    bool res3 = obj->search("aa");   // false;
    bool res4 = obj->search("a");    // true;
    bool res5 = obj->search(".a");   // false;
    bool res6 = obj->search("a.");   // false;

    if (res1 == true &&
        res2 == true &&
        res3 == false &&
        res4 == true &&
        res5 == false &&
        res6 == false
    )
        cout << "test2 success." << endl;
    else
        cout << "test2 failed." << endl;
}

int main()
{
    test1();
    test2();

    return 0;
}

// Design a data structure that supports the following two operations:

// void addWord(word)
// bool search(word)
// search(word) can search a literal word or a regular expression string containing only 
// letters a-z or .. A . means it can represent any one letter.

// Example:

// addWord("bad")
// addWord("dad")
// addWord("mad")
// search("pad") -> false
// search("bad") -> true
// search(".ad") -> true
// search("b..") -> true
// Note:
// You may assume that all words are consist of lowercase letters a-z.
