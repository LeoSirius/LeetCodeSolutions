### 思路1

```sql
SELECT s.id, s.name
FROM Students s LEFT JOIN Departments d
ON s.department_id=d.id
WHERE d.id IS NULL;
```
