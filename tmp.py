class Solution:
    def intToRoman(self, num: int) -> str:
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        M = ['', 'M', 'MM', 'MMM']
        return M[num // 1000] + C[num // 100 % 10] + X[num // 10 % 10] + I[num % 10]