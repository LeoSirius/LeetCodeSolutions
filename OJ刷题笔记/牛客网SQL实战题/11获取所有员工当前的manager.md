题目描述

```

```

sql

```sql
SELECT de.emp_no, dm.emp_no AS manager_no
FROM dept_emp AS de INNER JOIN dept_manager AS dm 
ON de.dept_no = dm.dept_no
WHERE de.to_date = '9999-01-01' AND dm.to_date = '9999-01-01' AND de.emp_no <> dm.emp_no
```

