#include<iostream>
using namespace std;

// class Solution{
// public:
// /*length 为字符数组str的总容量，大于或等于字符串str的实际长度*/
//     void ReplaceBlank(char str[], int length)
//     {
//     }
// };
class Solution{
public:
    void ReplaceBlank(char str[], int length)
    {
        if (str == nullptr || length <= 0) return;
        int len_origin = 0;
        int num_blanks = 0;
        for (int i = 0; str[i]; i++) {
            len_origin++;
            if (str[i] == ' ') num_blanks++;
        }

        int len_new = len_origin + 2 * num_blanks;
        if (len_new > length) return;

        int idx_origin = len_origin;
        int idx_new = len_new;
        while (idx_origin >= 0 && idx_new > idx_origin) {
            if (str[idx_origin] == ' ') {
                str[idx_new--] = '0';
                str[idx_new--] = '2';
                str[idx_new--] = '%';
            } else {
                str[idx_new--] = str[idx_origin];
            }
            idx_origin--;
        }
    }
};

// ====================测试代码====================
void Test(const char* testName, char str[], int length, char expected[])
{
    if(testName != nullptr)
        printf("%s begins: ", testName);

    Solution s;
    s.ReplaceBlank(str, length);

    if(expected == nullptr && str == nullptr)
        printf("passed.\n");
    else if(expected == nullptr && str != nullptr)
        printf("failed.\n");
    else if(strcmp(str, expected) == 0)
        printf("passed.\n");
    else
        printf("failed.\n");
}

// 空格在句子中间
void Test1()
{
    const int length = 100;

    char str[length] = "hello world";
    Test("Test1", str, length, "hello%20world");
}

// 空格在句子开头
void Test2()
{
    const int length = 100;

    char str[length] = " helloworld";
    Test("Test2", str, length, "%20helloworld");
}

// 空格在句子末尾
void Test3()
{
    const int length = 100;

    char str[length] = "helloworld ";
    Test("Test3", str, length, "helloworld%20");
}

// 连续有两个空格
void Test4()
{
    const int length = 100;

    char str[length] = "hello  world";
    Test("Test4", str, length, "hello%20%20world");
}

// 传入nullptr
void Test5()
{
    Test("Test5", nullptr, 0, nullptr);
}

// 传入内容为空的字符串
void Test6()
{
    const int length = 100;

    char str[length] = "";
    Test("Test6", str, length, "");
}

//传入内容为一个空格的字符串
void Test7()
{
    const int length = 100;

    char str[length] = " ";
    Test("Test7", str, length, "%20");
}

// 传入的字符串没有空格
void Test8()
{
    const int length = 100;

    char str[length] = "helloworld";
    Test("Test8", str, length, "helloworld");
}

// 传入的字符串全是空格
void Test9()
{
    const int length = 100;

    char str[length] = "   ";
    Test("Test9", str, length, "%20%20%20");
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();
    Test8();
    Test9();

    return 0;
}
