#include<stdio.h>
int main(){
    int outputBuf[82][82];
    char a, b;
    int n;
    bool isFirstCase = true;
    while(scanf("%d %c %c", &n, &a, &b) == 3){
        if(isFirstCase){
            isFirstCase = false;
        }else{
            printf("\n");           // 第一个测试用例之后的每个测试用例开头都有一空行
        }
        for(int i = 1, j = 1; i <= n; i += 2, j++){
            int x = n / 2 + 1;  // 先定位到中心
            x -= j - 1;
            int y = x;          // i是边长， j是圈数， x， y是右上角的坐标
            char c = (j % 2 == 1) ? a : b;      // ab交替出现
            for(int k = 0; k < i; k++){
                outputBuf[x+k][y] = c;      // 左
                outputBuf[x][y+k] = c;      // 上
                outputBuf[x+k][y+i-1] = c;  // 右
                outputBuf[x+i-1][y+k] = c;  // 下
            }
        }
        if(n != 1){
            outputBuf[1][n] = outputBuf[n][1] = outputBuf[1][1] = outputBuf[n][n] = ' ';
        }
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                printf("%c", outputBuf[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}