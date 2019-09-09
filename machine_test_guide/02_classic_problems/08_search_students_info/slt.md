### 思路1 排序后用二分查找

注意输入的学号不一定是有序的，所以先按学好进行排序，然后用二分查找。

```cpp
#include<iostream>
#include<algorithm>
using namespace std;

struct Student{
    int id;
    char name[10];
    char gender[5];
    int age;
    // 按学号升序排序
    bool operator < (const Student B)const{
        return id < B.id;
    }
};

void binary_sort_and_print(Student *students, int student_num, int target_id){
    int l = 0;
    int r = student_num - 1;
    while(l <= r){
        int mid = l + (r - l) / 2;
        int current_id = students[mid].id;
        if(current_id == target_id){
            printf("%02d %s %s %d\n", students[mid].id, students[mid].name, students[mid].gender, students[mid].age);
            break;
        }else if(current_id < target_id){
            l = mid + 1;
        }else{
            r = mid - 1;
        }
    }
}

int main(){
    int n, m;
    while(scanf("%d", &n) != EOF){
        Student *students = new Student[n];
        for(int i = 0; i < n; i++){
            scanf("%2d %s %s %d", &students[i].id, students[i].name, students[i].gender, &students[i].age);
        }
        scanf("%d", &m);
        sort(students, students+n);
        for(int i = 0; i < m; i++){
            int target_id;
            scanf("%d", &target_id);
            binary_sort_and_print(students, n, target_id);
        }
    }
    return 0;
}
```