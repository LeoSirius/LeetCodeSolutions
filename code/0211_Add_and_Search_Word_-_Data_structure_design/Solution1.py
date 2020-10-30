class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_end = False
        self.nexts = [None] * 26


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self
        for ch in word:
            if not node.nexts[ord(ch)-ord('a')]:
                node.nexts[ord(ch)-ord('a')] = WordDictionary()
            node = node.nexts[ord(ch)-ord('a')]
        node.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self
        if len(word) == 1:
            if word[0] == '.':
                for i in range(26):
                    if node.nexts[i] and node.nexts[i].is_end:
                        return True
            else:
                if node.nexts[ord(word[0]) - ord('a')] and node.nexts[ord(word[0]) - ord('a')].is_end:
                    return True
            return False
        
        if word[0] == '.':
            for i in range(26):
                if node.nexts[i] and node.nexts[i].search(word[1:]):
                    return True
        else:
            if node.nexts[ord(word[0]) - ord('a')]:
                return node.nexts[ord(word[0]) - ord('a')].search(word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def test1():
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')
    res1 = obj.search('pad')   # false
    res2 = obj.search('bad')   # true
    res3 = obj.search('.ad')   # true
    res4 = obj.search('b..')   # true

    if (res1, res2, res3, res4) == (False, True, True, True):
        print('test1 success.')
    else:
        print('test1 failed.')

def test2():
    obj = WordDictionary()
    obj.addWord('a')
    obj.addWord('a')
    res1 = obj.search('.')   # true
    res2 = obj.search('a')   # true
    res3 = obj.search('aa')  # false
    res4 = obj.search('a')   # true
    res5 = obj.search('.a')  # false
    res6 = obj.search('a.')  # false

    if (res1, res2, res3, res4, res5, res6) == (True, True, False, True, False, False):
        print('test2 success.')
    else:
        print('test2 failed.')


if __name__ == '__main__':
    test1()
    test2()


# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only 
# letters a-z or .. A . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
