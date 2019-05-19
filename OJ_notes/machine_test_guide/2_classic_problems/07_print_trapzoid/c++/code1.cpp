#include<stdio.h>
int main(){
    int h;
    while(scanf("%d", &h) != EOF){
        int maxCol = h + (h - 1) * 2;  // number of starts at bottom row
        for(int i = 0; i < h; i++){
            for(int j = 0; j < maxCol; j++){
                if(j < maxCol - (i * 2 + h)){
                    printf(" ");
                }else{
                    printf("*");
                }
            }
            printf("\n");
        }
    }
    return 0;
}