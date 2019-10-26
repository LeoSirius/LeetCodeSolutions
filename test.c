#include<stdio.h>
#include<string.h>

void
print_tokens (char *line)
{
    static char whitespace[] = " \t\n\r\v\f";   // 注意最前面有个空格
    char *token;
    for (token = strtok(line, whitespace);
        token != NULL;
        token = strtok(NULL, whitespace)) {
        printf("Next token is %s\n", token);
    }
}

int main ()
{
    char str[] = "leo love philosophy";
    print_tokens (str);
    printf("%s\n", str);        // 这行输出leo，源字符串已经被修改
    return 0;
}