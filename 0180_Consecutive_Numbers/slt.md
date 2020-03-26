### 思路1 三表联结

```sql
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.Num=l2.Num AND l2.Num=l3.Num AND l2.Id-1=l1.Id AND l3.Id-1=l2.Id;
```