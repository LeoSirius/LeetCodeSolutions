#include<stdio.h>
using namespace std;

int main(){
    int h;
    while(scanf("%d", &h) != EOF){
        int num_of_space = (h - 1) * 2;
        int num_of_star = h;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < num_of_space; j++){
                printf(" ");
            }
            for(int j = 0; j < num_of_star; j++){
                printf("*");
            }
            printf("\n");
            num_of_space -= 2;
            num_of_star += 2;
        }
    }
    return 0;
}