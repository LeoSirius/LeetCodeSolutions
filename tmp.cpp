#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

struct Student
{
    unsigned int id;
    string name;
    string gender;
    unsigned int age;

    bool
    operator < (Student const &another) const {
        return id < another.id;
    }
};

void find_and_print(vector<Student> &students, int target_id)
{
    int l, r, m;
    l = 0; r = students.size() - 1;
    while (l <= r) {
        m = l + (r - l) / 2;
        if (students[m].id == target_id) {
            printf("%02d %s %s %d\n", students[m].id, students[m].name.c_str(), students[m].gender.c_str(), students[m].age);
            break;
        } else if (target_id < students[m].id) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
}

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<Student> students;
        Student tmp_student;
        for (int i = 0; i < n; i++) {
            cin >> tmp_student.id >> tmp_student.name
                >> tmp_student.gender >> tmp_student.age;
            students.push_back(tmp_student);
        }
        int m; scanf("%d", &m);
        sort(students.begin(), students.end());
        for (int i = 0; i < m; i++) {
            int target_id;
            scanf("%d", &target_id);
            find_and_print(students, target_id);
        }
    }
    return 0;
}

