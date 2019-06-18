#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

struct Student{
    char name[101];
    int age;
    int score;
    bool operator < (const Student S) const{
        if(score != S.score){
            return score < S.score;
        }else{
            return strcmp(name, S.name) < 0;
        }
    }
};
Student s[1000];
int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            scanf("%s %d %d", s[i].name, &s[i].age, &s[i].score);
        }
        sort(s, s + n);
        for(int i = 0; i < n; i++){
            printf("%s %d %d\n", s[i].name, s[i].age, s[i].score);
        }
    }
    return 0;
}