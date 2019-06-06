#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;

struct Student{
    char no[3];
    char name[20];
    char gender[5];
    int age;
    bool operator < (const Student B)const{
        return strcmp(no, B.no) < 0;
    }
};

int main(){
    int n;
    Student S[1000];
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            scanf("%s %s %s %d", S[i].no, S[i].name, S[i].gender, &S[i].age);
        }
        sort(S, S + n);
        int m;
        scanf("%d", &m);
        for(int i = 0; i < m; i++){
            char x[3];
            scanf("%s", x);
            int left = 0, right = n - 1;
            int mid;
            while(left <= right){
                mid = left + ((right - left)/ 2);
                int tmp = strcmp(x, S[mid].no);
                if(tmp == 0){
                    printf("%s %s %s %d\n", S[mid].no, S[mid].name, S[mid].gender, S[mid].age);
                    break;
                }else if(tmp < 0){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }
            if(left > right){
                printf("No Answer!\n");
            }
        }
    }
    return -1;
}