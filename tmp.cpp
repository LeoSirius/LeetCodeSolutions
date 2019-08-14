#include<iostream>
using namespace std;

int main(){
    int a, b;
    while(scanf("%d %d", &a, &b) != EOF && !(a == 0 && b == 0)){
        int res = 1;
        // 
        // 若b是偶数，如8，a按循环会依次等于b=4,a^2, b=2,a^4, b=1,a^8, 
        // 若b是奇数，如7，a按循环会依次等于res=a,b=3,a^2, res=a^3,b=1,a^4, res=a^4,b=0 over
        while(b){
            if(b % 2 == 1){
                res *= a;
                res %= 1000;
            }
            b /= 2;
            a *= a;
            a %= 1000;
        }
        printf("%d\n", res);
    }
    return 0;
}