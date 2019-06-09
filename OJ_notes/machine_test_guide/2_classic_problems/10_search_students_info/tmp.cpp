#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

struct Student{
    char num[3];
    char name[10];
    char gender[5];
    int age;
    bool operator < (const Student S) const{
        int tmp = strcmp(num, S.num);
        return tmp < 0;
    }
};

Student stu_array[1000];

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        char num[3], name[10], gender[5];
        int age;
        for(int i = 0; i < n; i++){
            scanf("%s %s %s %d", stu_array[i].num, stu_array[i].name, stu_array[i].gender, &stu_array[i].age);
        }
        sort(stu_array, stu_array + n);
        int m;
        scanf("%d", &m);
        for(int i = 0; i < m; i++){
            char target_num[3];
            scanf("%s", target_num);
            int l = 0, r = m - 1;
            int mid;
            while(l <= r){
                mid = l + (r - l) / 2;
                int tmp = strcmp(stu_array[mid].num, target_num);
                if(tmp == 0){
                    printf("%s %s %s %d\n", target_num, stu_array[mid].name, stu_array[mid].gender, stu_array[mid].age);
                    break;
                }else if(tmp > 0){
                    r = mid - 1;
                }else{
                    l = mid + 1;
                }
            }
            if(l > r){
                printf("No Answer!");
            }
        }
    }
    return 0;
}