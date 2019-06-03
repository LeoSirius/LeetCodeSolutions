#include<stdio.h>
using namespace std;

int main(){
    char buf[82][82];
    int n;
    char a, b;
    bool is_frist_case = true;
    while(scanf("%d %c %c", &n, &a, &b) == 3){
        if(is_frist_case)
            is_frist_case = false;
        else{
            printf("\n");
        }
        for(int i = 1, j = 1; i <= n; i += 2, j++){
            int x = n / 2 + 1;
            x -= j - 1;
            int y = x;
            char current_char = (j % 2 == 1 ? a : b);
            for(int k = 0; k < i; k++){
                buf[x][y + k] = current_char;
                buf[x + i - 1][y + k] = current_char;
                buf[x + k][y] = current_char;
                buf[x + k][y + i - 1] = current_char;
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
    return 0;
}