/**
 * Initialize your data structure here.
 */
var Trie = function() {
  this.is_end = false;
  this.nexts = Array(26).fill(null);
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
  node = this;
  let a_ascii = 'a'.charCodeAt(0);
  for (const ch of word) {
    if (!node.nexts[ch.charCodeAt(0) - a_ascii]) {
      node.nexts[ch.charCodeAt(0) - a_ascii] = new Trie();
    }
    node = node.nexts[ch.charCodeAt(0) - a_ascii];
  }
  node.is_end = true;
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
  node = this;
  let a_ascii = 'a'.charCodeAt(0);
  for (const ch of word) {
    if (!node.nexts[ch.charCodeAt(0) - a_ascii]) {
      return false;
    }
    node = node.nexts[ch.charCodeAt(0) - a_ascii];
  }
  return node.is_end;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
  node = this;
  let a_ascii = 'a'.charCodeAt(0);
  for (const ch of prefix) {
    if (!node.nexts[ch.charCodeAt(0) - a_ascii]) {
      return false;
    }
    node = node.nexts[ch.charCodeAt(0) - a_ascii];
  }
  return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */


function is_equal_array(arr1, arr2) {
  if (!Array.isArray(arr1) || !Array.isArray(arr2))
    return false;
  if (arr1.length != arr2.length)
    return false;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] != arr2[i])
      return false;
  }
  return true;
}

function test1() {
  var obj = new Trie();
  obj.insert('apple');
  var res1 = obj.search('apple');   // true
  var res2 = obj.search('app');     // false
  var res3 = obj.startsWith('app'); // true
  obj.insert('app');
  var res4 = obj.search('app');     // true
  if (is_equal_array([res1, res2, res3, res4], [true, false, true, true]))
    console.log('test1 success.');
  else
    console.log('test1 failed.');
}

test1();


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
