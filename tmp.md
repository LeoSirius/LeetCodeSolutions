### 题目描述

有N个学生的数据，将学生数据按照成绩从低到高排序，如果成绩相同则按照姓名字符的字母排序，如果姓名的字母顺序也相同则按照学生的年龄排序，并输出N个学生排序后的信息。

### 输入

测试数据有多组，每组输入第一行有一个整数N(N <= 1000)，接下来的N行包括N个学生的数据。每个学生的数据包括姓名（长度不超过100的字符串）、年龄（整数型）、成绩（小于等于100的整数）。

### 输出

将学生信息按成绩进行排序，成绩相同的则按姓名的字母顺序进行排序。然后输出学生信息。按照如下格式输出：姓名 年龄 成绩

### 样例输入

```
3
abc 20 99
bcd 19 97
bed 20 97
```

### 样例输出

```
bcd 19 97
bed 20 97
abc 20 99
```

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