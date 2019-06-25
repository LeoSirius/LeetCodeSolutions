class Solution {
public:
    string intToRoman(int num) {
        string I[10] = {"", "I","II","III","IV","V","VI","VII","VIII","IX"};
        string X[10] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string C[10] = {"", "C", "CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string M[4] = {"", "M","MM","MMM"};
        return M[num/1000]+C[num/100%10]+X[num/10%10]+I[num%10];
    }
};