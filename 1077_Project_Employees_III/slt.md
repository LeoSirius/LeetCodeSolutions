### 思路1

因为可能用相同的情况，所以不能直接GROUP + MAX来选。

找到每个项目中最长year的year数，并同project_id一起返回

```sql
SELECT p.project_id, MAX(e.experience_years) AS experience_years
FROM Project p JOIN Employee e
ON p.employee_id=e.employee_id
GROUP BY p.project_id;
```

在联机两表，找到experience_years=MAX(experience_years)的员工即可
联结两表是为了获取那个员工所在project的project_id

```sql
SELECT p.project_id, e.employee_id
FROM Project p JOIN Employee e
ON p.employee_id=e.employee_id
WHERE (p.project_id, e.experience_years)
IN (
  SELECT p.project_id, MAX(e.experience_years) AS experience_years
  FROM Project p JOIN Employee e
  ON p.employee_id=e.employee_id
  GROUP BY p.project_id
);
```
