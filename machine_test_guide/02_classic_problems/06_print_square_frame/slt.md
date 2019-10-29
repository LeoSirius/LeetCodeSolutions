## 思路1 先排版 再输出

先用一个缓存数组排版，然后再输出。

注意排版时，先排左边和上边，再排右边和下边。右边和下边的个数自然少一个。最后再把四个角置为空格。

另外要注意字符的输入和停止的条件。如果scanf中没有空格，则输入的空格会被当成字符输入。
`while(scanf("%d %c %c", &n, &a, &b) == 3)`

```cpp
#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int size;
    char i_ch, o_ch;
    while (scanf("%d %c %c", &size, &i_ch, &o_ch) != EOF) {
        vector<vector<int>> buf(size, vector<int> (size, 0));
        int num_of_circle = 0;
        for (int cur_size = 1; cur_size <= size; cur_size += 2) {
            num_of_circle++;
            char cur_char = num_of_circle % 2 == 1 ? i_ch : o_ch;
            int x, y;        //  x, y为当期安圈左上角的那个坐标，先定位到中心，在减去当前边长的一半。xy都是从0开始
            x = (size / 2) - (cur_size / 2);
            y = x;
            for (int i = 0; i < cur_size; i++) {
                buf[x][y + i] = cur_char;
                buf[x + cur_size - 1][y + i] = cur_char;
                buf[x + i][y] = cur_char;
                buf[x + i][y + cur_size - 1] = cur_char;
            }
            if (size > 1) {
                buf[0][size-1] = buf[size-1][0] = buf[0][0] = buf[size-1][size-1] = ' ';
            }
        }
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                printf("%c", buf[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
```