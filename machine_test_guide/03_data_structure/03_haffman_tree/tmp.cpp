#include<iostream>
#include<queue>
#include<vector>
using namespace std;
priority_queue<int, vector<int>, greater<int> > Q;

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        for(int i = 0; i < n; i++){
            int input_num;
            scanf("%d", &input_num);
            Q.push(input_num);
        }
        int res = 0;
        // if only one element left in queue, that is the root node of haffman tree
        // that node's value does not count in answer.
        while(Q.size() >= 2){
            int a = Q.top(); Q.pop();
            int b = Q.top(); Q.pop();
            res += a + b;
            Q.push(a + b);
        }
        printf("%d\n", res);
    }
    return 0;
}