#include<iostream>
#include<cstring>    // strtok在此库
using namespace std;
int main(){
    char str[] = "- This, a sample string OK.";
    // 下面从str逐个抽取被" ,.-"这四个字符分割的字符串
    char *p = strtok(str, " ,.-");
    // 只要p不为空，就说明找到了一个子串
    while(p != NULL){
        cout << p << endl;
        // 后续调用，第一个参数必须是NULL
        p = strtok(NULL, " ,.-");
    }
    return 0;
}