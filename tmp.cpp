class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        for (int i = 0; strs.size() > 0; res += strs[0][i++]) {
            for (int j = 0; j < strs.size(); j++) {
                if (i >= strs[j].size() || j > 0 && strs[j-1][i] != strs[j][i])
                    return res;
            }
        }
        return res;
    }
};