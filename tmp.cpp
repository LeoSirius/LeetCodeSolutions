#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        int *nums = new int[n];
        for(int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            nums[i] = x;
        }
        sort(nums, nums+n);
        for(int i = 0; i < n; i++){
            printf("%d ", nums[i]);
        }
        printf("\n");
        delete [] nums;
    }
}