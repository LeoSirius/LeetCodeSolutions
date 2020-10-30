#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "meta_c/utils.h"

char* reverseLeftWords(char* s, int n){
    int len = strlen(s);
    char *left_chars = malloc(sizeof(char) * n + 1);
    memcpy(left_chars, s, n);
    left_chars[n] = '\0';

    for (int i = n; s[i]; i++)
        s[i-n] = s[i];

    int new_right_start = len - n;
    for (int i = 0; i < n; i++)
        s[i+new_right_start] = left_chars[i];
    return s;
}

void test(char *test_name, char *s, int n, char *expected)
{
    char *res = reverseLeftWords(s, n);
    if (is_equal_str(expected, res))
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}



int main()
{
    char s1[] = "abcdefg";
    int k1 = 2;
    char expected1[] = "cdefgab";
    test("test1", s1, k1, expected1);

    char s2[] = "lrloseumgh";
    int k2 = 6;
    char expected2[] = "umghlrlose";
    test("test2", s2, k2, expected2);


    return 0;
}

// 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
// 请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
// 该函数将返回左旋转两位得到的结果"cdefgab"。

// 示例 1：

// 输入: s = "abcdefg", k = 2
// 输出: "cdefgab"

// 示例 2：

// 输入: s = "lrloseumgh", k = 6
// 输出: "umghlrlose"
//  

// 限制：

// 1 <= k < s.length <= 10000

