#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

struct Student
{
    Student(int id, string name, string gender, int score)
        :id(id), name(name), gender(gender), score(score) {}
    int id;
    string name;
    string gender;
    int score;
};

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<Student> students;
        for (int i = 0; i < n; i++) {
            int id, score; string name, gender;
            cin >> id >> name >> gender >> score;
            Student student(id, name, gender, score);
            students.push_back(student);
        }
        int m; scanf("%d", &m);
        while (m--) {
            int target_id; scanf("%d", &target_id);
            int left = 0, right = students.size() - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (target_id > students[mid].id) left = mid + 1;
                else if (target_id < students[mid].id) right = mid - 1;
                else {
                    cout << students[mid].id << " " << students[mid].name << " " << students[mid].gender << " " << students[mid].score << endl;
                    break;
                }
            }
        }
    }
    return 0;
}