#include<iostream>
#include<algorithm>
using namespace std;

struct Goods{
    double f;
    double j;
    double s;
    bool operator < (const Goods b) const{
        return s > b.s;
    }
};

Goods goods[1000];

int main(){
    double m;
    int n;
    while(scanf("%lf%d", &m, &n) != EOF && (m != -1 && n != -1)){
        for(int i = 0; i < n; i++){
            scanf("%lf %lf", &goods[i].j, &goods[i].f);
            goods[i].s = goods[i].j / goods[i].f;
        }
        sort(goods, goods + n);
        int idx = 0;
        double res = 0;
        while(m > 0 && idx < n){
            if(m > goods[idx].f){
                res += goods[idx].j;
                m -= goods[idx].f;
            }else{
                res += goods[idx].s * m;
                m = 0;
            }
            idx++;
        }
        printf("%.3lf\n", res);
    }
}