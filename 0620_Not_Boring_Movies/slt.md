### 思路1

```sql
SELECT *
FROM cinema
WHERE description!="boring" AND MOD(id,2)=1
ORDER BY rating DESC;
```
