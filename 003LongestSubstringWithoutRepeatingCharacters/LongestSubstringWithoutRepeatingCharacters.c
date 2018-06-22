class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		vector<int> dict(256, -1);
		int maxLen = 0, start = -1;
		for (int i = 0; i != s.length(); i++) {
			if (dict[s[i]] > start)
				start = dict[s[i]];
			dict[s[i]] = i;
			maxLen = max(maxLen, i - start);
		}
		return maxLen;
	}
};

利用ascii码的性质，用数组下标作为k，值作为v来构建一个映射。
start存储上次重复出现的字母两个中前一个的下标，开始为-1。因此当前的i-start之间所有元素都不重复
第一次出现的字母dict[s[i]]为-1，不大于start
一旦字母访问一次，便把索引给dict[s[i]]。字母一旦重复出现，便会大于start