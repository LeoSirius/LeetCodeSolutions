#include<iostream>
#include<queue>
using namespace std;

priority_queue<int, vector<int>, greater<int> > Q;

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        while(!Q.empty()) Q.pop();
        for(int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            Q.push(x);
        }
        int res = 0;
        while(Q.size() > 1){
            int a, b;
            a = Q.top();
            Q.pop();
            b = Q.top();
            Q.pop();

            res += a + b;
            Q.push(a + b);
        }
        printf("%d\n", res);
    }
    return 0;
}