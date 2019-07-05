#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

struct Student{
    string name;
    int age;
    int score;
    bool operator <(const Student B) const{
        if(score != B.score)
            return score < B.score;
        else{
            return name < B.name;
        }
    }
};

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        vector<Student> students(n);
        for(int i = 0; i < n; i++){
            cin >> students[i].name >> students[i].age >> students[i].score;
        }
        sort(students.begin(), students.end());
        for(int i = 0; i < n; i++){
            cout << students[i].name << " " << students[i].age << " " << students[i].score << endl;
        }
    }
    return 0;
}