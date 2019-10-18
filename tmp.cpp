#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct Student
{
    string name;
    int age;
    int score;
    bool operator < (Student const &other) const
    {
        if (score != other.score) {
            return score < other.score;
        } else {
            return name < other.name;
        }
    }
};

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<Student> students;
        for (int i = 0; i < n; i++) {
            Student stu;
            cin >> stu.name >> stu.age >> stu.score;
            students.push_back(stu);
        }
        sort(students.begin(), students.end());
        for (int i = 0; i < n; i++) {
            cout << students[i].name << " " << students[i].age << " " << students[i].score << endl;
        }
    }
    return 0;
}