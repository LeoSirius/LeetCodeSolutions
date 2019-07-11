#include<iostream>
using namespace std;

struct Student{
    int id;
    char name[10];
    char gender[5];
    int age;
    bool operator < (const Student &B) const{
        return id < B.id;
    }
};

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        Student *students = new Student[n];
        for(int i = 0; i < n; i++){
            scanf("%d %s %s %d", &students[i].id, students[i].name, students[i].gender, &students[i].age);
        }
        sort(students, students+n);
        int m;
        scanf("%d", &m);
        while(m--){
            int target_id;
            scanf("%d", &target_id);
            int left = 0;
            int right = n-1;
            while(left <= right){
                int mid = left + (right - left) / 2;
                if(target_id == students[mid].id){
                    printf("%02d %s %s %d\n", students[mid].id, students[mid].name, students[mid].gender, students[mid].age);
                    break;
                }else if(target_id > students[mid].id){
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            }
        }
    }
    return 0;
}