#include<iostream>
using namespace std;

int main(){
    int h;
    while(scanf("%d", &h) != EOF){
        int num_of_blank = (h - 1) * 2;
        int num_of_cols = num_of_blank + h;
        for(int i = 0; i < h; i++){
            int j = 0;
            for(; j < num_of_blank; j++){
                printf(" ");
            }
            num_of_blank -= 2;
            for(; j < num_of_cols; j++){
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}