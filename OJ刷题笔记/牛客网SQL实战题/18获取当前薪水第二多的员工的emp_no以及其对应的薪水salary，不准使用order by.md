题目描述

```

```

sql

```sql
SELECT e.emp_no, MAX(s.salary) AS salary, e.last_name, e.first_name
FROM employees AS e INNER JOIN salaries AS s
ON e.emp_no = s.emp_no 
WHERE s.to_date = '9999-01-01' AND salary != (SELECT MAX(salary) FROM salaries WHERE to_date = '9999-01-01');
```

