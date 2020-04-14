### 思路1

这道题改id就行了，最后再排序

```sql
SELECT 
    CASE
        WHEN MOD(id, 2) != 0 AND id!=cnt THEN id + 1  -- id是奇数，且不是最后一个
        WHEN MOD(id, 2) != 0 AND id=cnt THEN id       -- id是奇数，是最后一个
        ELSE id -1   -- id是偶数
    END AS id
,
student
FROM seat JOIN (
SELECT COUNT(*) AS cnt
FROM seat) AS t
ORDER BY id;
```
