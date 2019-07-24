## 思路1 重写结构体的小于运算符

注意题目叫我们从小到大排序，可以看出是排升序。

```cpp
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

struct Student{
    string name;
    int age;
    int score;
    bool operator < (const Student &b) const{
        if(score != b.score){
            return score < b.score;
        }else{
            return name < b.name;
        }
    }
};

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        Student *students = new Student[n];
        for(int i = 0; i < n; i++){
            cin >> students[i].name;
            cin >> students[i].age;
            cin >> students[i].score;
        }
        sort(students, students + n);
        for(int i = 0; i < n; i++){
            cout << students[i].name << ' ' << students[i].age << ' ' << students[i].score << endl;
        }
    }
    return 0;
}
```