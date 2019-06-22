#include<iostream>
using namespace std;

int main(){
    int *parray = new int[100](1);
    for(int i = 0; i < 100; i++){
        printf("%d\n", parray[i]);
    }
    return 0;
}