题目描述

```

```

sql

```sql
SELECT s1.emp_no, s1.salary, COUNT(DISTINCT s2.salary) as rank
FROM salaries as s1, salaries as s2
WHERE s1.to_date = '9999-01-01' AND s2.to_date = '9999-01-01' AND s1.salary <= s2.salary
GROUP BY s1.emp_no
ORDER BY s1.salary DESC, s1.emp_no ASC
```

