/**
 * @param {string[]} words
 */
var WordDistance = function(words) {
  this.mp = {};
  for (let i = 0; i < words.length; i++) {
    if (this.mp.hasOwnProperty(words[i])) {
      this.mp[words[i]].push(i);
    } else {
      this.mp[words[i]] = [i];
    }
  }
};

/** 
 * @param {string} word1 
 * @param {string} word2
 * @return {number}
 */
WordDistance.prototype.shortest = function(word1, word2) {
  let res = Number.MAX_SAFE_INTEGER;
  for (let i of this.mp[word1]) {
    for (let j of this.mp[word2]) {
      res = Math.min(res, Math.abs(i-j));
    }
  }
  return res;
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * var obj = new WordDistance(words)
 * var param_1 = obj.shortest(word1,word2)
 */

function test(test_name, words, word1, word2, expected) {
  let obj = new WordDistance(words);
  let res = obj.shortest(word1, word2);
  if (res === expected) {
    console.log(test_name + ' success.');
  } else {
    console.log(test_name + ' failed.');
  }
}


let words = ["practice", "makes", "perfect", "coding", "makes"];

let word11 = "coding";
let word21 = "practice";
let expected1 = 3;
test("test1", words, word11, word21, expected1);

let word12 = "makes";
let word22 = "coding";
let expected2 = 1;
test("test2", words, word12, word22, expected2);



// Design a class which receives a list of words in the constructor, 
// and implements a method that takes two words word1 and word2 and return 
// the shortest distance between these two words in the list. 
// Your method will be called repeatedly many times with different parameters. 

// Example:
// Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

// Input: word1 = “coding”, word2 = “practice”
// Output: 3
// Input: word1 = "makes", word2 = "coding"
// Output: 1
// Note:
// You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


