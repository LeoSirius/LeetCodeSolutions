class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        is_end = False
        nexts = [None] * 26


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            if not node.nexts[ord(ch)-ord('a')]:
                node.nexts = Trie()
            node = node.nexts
        node.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for ch in word:
            node = node.nexts[ord(ch)-ord('a')]
            if not node:
                return False
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for ch in word:
            node = node.nexts[ord(ch)-ord('a')]
            if not node:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def test1():
    obj = Trie()
    obj.insert('apple')
    res1 = obj.search('apple')    # True
    res2 = obj.search('app')      # Flase
    res3 = obj.startsWith('app')  # True
    obj.insert('app')
    res4 = obj.search('app')      # True

    if (res1, res2, res3, res4) == (True, False, True, True):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == '__main__':
    test1()


# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.