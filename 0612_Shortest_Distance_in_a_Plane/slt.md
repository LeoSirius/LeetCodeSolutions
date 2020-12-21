### 思路1 JOIN计算每两点之间的距离

注意这里的不等联结，一定要把多列括起来，不然判断的就是单列的不等

```sql
SELECT ROUND(
  MIN(SQRT(ABS(p2.y-p1.y)*ABS(p2.y-p1.y) + ABS(p2.x-p1.x)*ABS(p2.x-p1.x)))
  , 2)
AS shortest
FROM point_2d p1 JOIN point_2d p2
ON (p1.x, p1.y)!=(p2.x, p2.y);
```
