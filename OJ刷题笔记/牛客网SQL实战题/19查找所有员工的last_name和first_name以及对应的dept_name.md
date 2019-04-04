题目描述

```

```

sql

```sql
SELECT e.last_name, e.first_name, dp.dept_name
FROM (employees AS e LEFT JOIN dept_emp AS de ON e.emp_no = de.emp_no)
LEFT JOIN departments AS dp 
ON de.dept_no = dp.dept_no;
```

