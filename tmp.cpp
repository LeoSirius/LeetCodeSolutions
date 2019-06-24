#include<iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x != 0 && x % 10 == 0))
            return false;
        int sum = 0;
        while(sum < x){
            sum = sum*10 + x%10;
            x /= 10;
        }
        // each represent case of "123321" and "12321"
        return x==sum || x == sum/10;
    }
};

int main(){
    Solution s = Solution();
    cout << s.isPalindrome(123321) << endl;
}
