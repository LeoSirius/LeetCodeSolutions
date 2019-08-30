## 思路1 重写结构体的小于运算符

注意题目叫我们从小到大排序，可以看出是排升序。

```cpp
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

struct Student
{
    string name;
    int age, score;

    bool
    operator < (Student const &B) const
    {
        if (score != B.score) {
            return score < B.score;
        } else {
            if (name != B.name) {
                return strcmp(name.c_str(), B.name.c_str()) < 0;
            } else {
                return age < B.age;
            }
        }
    }
};

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<Student> students;
        for (int i = 0; i < n; i++) {
            Student student;
            cin >> student.name >> student.age >> student.score;
            students.push_back(student);
        }
        sort(students.begin(), students.end());
        for (int i = 0; i < n; i++) {
            printf("%s %2d %2d\n", students[i].name.c_str(), students[i].age, students[i].score);
        }
    }
    return 0;
}
```