class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        for (int p = 0; strs.size(); prefix += strs[0][p++]) {
            for (int i = 0; i < strs.size(); i++) {
                if (p >= strs[i].size() || i && strs[i][p] != strs[i-1][p])
                    return prefix;
            }
        }
        return prefix;
    }
};