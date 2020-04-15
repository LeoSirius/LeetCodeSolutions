因为可能用相同的情况，所以不能直接GROUP + MAX来选。

先找出每个project_id及其对应的人员的最大年限数量

```sql
SELECT p.project_id, MAX(e.experience_years)
FROM Project p JOIN Employee e
ON p.employee_id=e.employee_id
GROUP BY p.project_id;
```

再表用子查询WHERE IN

```sql
SELECT p.project_id, e.employee_id
FROM Project p JOIN Employee e
ON p.employee_id=e.employee_id
WHERE (p.project_id, e.experience_years) IN (
    SELECT p.project_id, MAX(e.experience_years)
    FROM Project p JOIN Employee e
    ON p.employee_id=e.employee_id
    GROUP BY p.project_id
)
```
