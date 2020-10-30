### 思路1 使用GROUP BY

```sql
SELECT Email
FROM Person
GROUP BY Email
HAVING Count(Email) > 1;
```