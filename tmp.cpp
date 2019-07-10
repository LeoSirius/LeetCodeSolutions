class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();

        // i的上届是等于m-n的，如m=10， n=3，i最后等于7，最后还剩两个格子，加上i本身正好是3
        for(int i = 0; i <= (m - n); ++i){
            int j = 0;
            for(; j < n; ++j){
                if(haystack[i+j] != needle[j]){
                    break;
                }
            }
            if(j == n){
                return i;
            }
        }
        return -1;
    }
};