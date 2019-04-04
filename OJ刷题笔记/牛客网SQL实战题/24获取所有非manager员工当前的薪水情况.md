题目描述

```

```

sql

```sql
SELECT de.dept_no, e.emp_no, s.salary 
FROM (employees as e INNER JOIN salaries as s ON e.emp_no = s.emp_no AND s.to_date = '9999-01-01')
INNER JOIN dept_emp as de ON de.emp_no = e.emp_no
WHERE de.emp_no NOT IN (SELECT emp_no FROM dept_manager)
```

