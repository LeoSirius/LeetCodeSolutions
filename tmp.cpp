class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == INT_MIN && divisor == -1){
            return INT_MAX;
        }
        long dvd = labs(dividend), dvs = labs(divisor), ans = 0;
        int sign = dividend > 0 ^ divisor > 0 ? -1 : 1;
        while(dvd >= dvs){
            long i_times_of_dvs = dvs, i = 1;
            while(i_times_of_dvs << 1 <= dvd){
                i_times_of_dvs <<= 1;
                i <<= 1;
            }
            dvd -= i_times_of_dvs;
            ans += i;
        }
        return sign * ans;
    }
};