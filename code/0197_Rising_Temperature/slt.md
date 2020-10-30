### 思路1

使用内联结，然后用DATEDIFF或TO_DAYS比较日期。

DATEDIFF(A, B)的结果是A-B。如A="2019-10-11", B="2019-10-10",则DATEDIFF(A, B)=1, DATEDIFF(B, A)=-1

```sql
SELECT w1.Id
FROM Weather w1 INNER JOIN Weather w2
ON DATEDIFF(w1.RecordDate, w2.RecordDate)=1 AND w1.Temperature > w2.Temperature;
```
