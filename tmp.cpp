#include<iostream>
using namespace std;

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        for (int x = 0; x <= 100; x++) {
            for (int y = 0; x + y <= 100; y++) {
                int z = 100 - x - y;
                // 这里都乘3，避免了除法带来的精度损失
                if (x * 5 * 3 + y * 3 * 3 + z <= n * 3)
                    printf("x=%d, y=%d, z=%d\n", x, y, z);
            }
        }
        printf("\n");
    }
    return 0;
}