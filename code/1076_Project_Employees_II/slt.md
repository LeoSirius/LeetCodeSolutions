### 思路1

关键是要处理多个COUNT相等的情况。我们可以先把COUNT的max值取出来作为子查询

```sql
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id)=(
    SELECT COUNT(employee_id) FROM Project
    GROUP BY project_id
    ORDER BY COUNT(employee_id) DESC LIMIT 1
);
```
