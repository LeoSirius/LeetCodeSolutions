class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1 || numRows >= s.size()) return s;

        vector<string> strs(numRows, "");
        int step = 1, idx = 0;
        for(int i = 0; i < s.size(); i++){
            strs[idx] += s[i];
            idx += step;
            if(idx == 0) step = 1;
            else if(idx == numRows-1) step = -1;
        }
        string res = "";
        for(int i = 0; i < strs.size(); i++) res += strs[i];
        return res;
    }
};