## 思路1 先排版 再输出

先用一个缓存数组排版，然后再输出。

注意排版时，先排左边和上边，再排右边和下边。右边和下边的个数自然少一个。最后再把四个角置为空格。

另外要注意字符的输入和停止的条件。如果scanf中没有空格，则输入的空格会被当成字符输入。
`while(scanf("%d %c %c", &n, &a, &b) == 3)`

```cpp
#include<iostream>
using namespace std;

int
main ()
{
    int n;
    char a, b;
    while (scanf("%d %c %c", &n, &a, &b) != EOF) {
        int buffer[81][81] = {0};
        int num_of_circle = 0;
        char cur_char;
        for (int cur_size = 1; cur_size <= n; cur_size += 2) {
            num_of_circle++;
            cur_char = num_of_circle % 2 == 1 ? a : b;
            int x, y;        //  x, y为左上角的那个坐标，先定位到中心，在减去当前边长的一半。xy都是从0开始
            x = (n / 2) - (cur_size / 2);
            y = x;
            for (int i = 0; i < cur_size; i++) {
                buffer[x][y+i] = cur_char;
                buffer[x+cur_size-1][y+i] = cur_char;
                buffer[x+i][y] = cur_char;
                buffer[x+i][y+cur_size-1] = cur_char;
            }
        }
        if (n > 1) {
            buffer[0][0] = buffer[0][n-1] = buffer[n-1][0] = buffer[n-1][n-1] = ' ';
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                printf("%c", buffer[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
}
```