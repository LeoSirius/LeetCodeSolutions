#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

struct Student{
    char no[100];
    char name[100];
    int age;
    char sex[5];
    bool operator < (const Student & A) const{
        return strcmp(no, A.no) < 0;
    }
}buf[1000];

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            scanf("%s%s%s%d", buf[i].no, buf[i].name, buf[i].sex, &buf[i].age);
        }
        sort(buf, buf + n);
        int t;
        scanf("%d", &t);    // t组查询
        while(t--){
            int ans = -1;   // 目标元素的下标，初始化为-1
            char x[30];
            scanf("%s", x); // 待查找的学号
            int right = n - 1, left = 0;
            int mid;
            while(left <= right){
                mid = (left + right) / 2;
                int tmp = strcmp(buf[mid].no, x);  // strcmp用ascii码比较的结果正好就是数字比较的结果
                if(tmp == 0){
                    ans = mid;
                    break;
                }else if(tmp > 0) 
                    right = mid - 1;
                else 
                    left = mid + 1;
            }
            if(ans == -1)
                printf("No Answer!\n");
            else
                printf("%s %s %s %d\n", buf[ans].no, buf[ans].name, buf[ans].sex, buf[ans].age);
        }
    }
    return 0;
}