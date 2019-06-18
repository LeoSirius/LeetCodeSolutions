#include<iostream>
using namespace std;

int main(){
    int n;
    char a, b;
    bool is_first_case = true;
    int buf[82][82];
    while(scanf("%d %c %c", &n, &a, &b) != EOF){
        if(is_first_case){
            is_first_case = false;
        }else{
            printf("\n");
        }
        for(int i = 1, j = 1; i <= n; i += 2, j++){
            int x = n / 2 + 1;
            x -= j - 1;
            int y = x;
            char c = (j % 2 == 1) ? a : b;
            for(int k = 0; k < i; k++){
                buf[x][y+k] = c;
                buf[x+i-1][y+k] = c;
                buf[x+k][y] = c;
                buf[x+k][y+i-1] = c;
            }
        }
        if(n != 1){
            buf[1][1] = buf[1][n] = buf[n][1] = buf[n][n] = ' ';
        }
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                printf("%c", buf[i][j]);
            }
            printf("\n");
        }
    }
}