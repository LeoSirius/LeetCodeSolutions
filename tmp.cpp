class Solution {
public:
    vector<string> letterCombinations(string digits) {
        map<int, string> num2alpha = {
            {2, "abc"},
            {3, "def"},
            {4, "ghi"},
            {5, "jkl"},
            {6, "mno"},
            {7, "pqrs"},
            {8, "tuv"},
            {9, "wxyz"},
        };
        vector<string> res;
        if (digits.size() == 0) return res;
        res.push_back("");
        for (int i = 0; i < digits.size(); i++) {
            vector<string> tmp_res;
            string chars = num2alpha[digits[i] - '0'];
            for (int c = 0; c < chars.size(); c++) {
                for (int j = 0; j < res.size(); j++) {
                    tmp_res.push_back(res[j]+chars[c]);
                }
            }
            res = tmp_res;
        }
        return res;
    }
};