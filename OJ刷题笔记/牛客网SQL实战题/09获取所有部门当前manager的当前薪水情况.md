题目描述

```

```

sql

```sql
SELECT d.dept_no, d.emp_no, s.salary 
FROM salaries AS s INNER JOIN dept_manager AS d
ON d.emp_no = s.emp_no AND d.to_date = '9999-01-01' AND s.to_date = '9999-01-01';
```

