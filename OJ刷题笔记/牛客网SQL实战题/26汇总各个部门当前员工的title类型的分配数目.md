题目描述

```

```

sql

```sql
SELECT de.dept_no , dp.dept_name, t.title, COUNT(t.title) as count
FROM dept_emp de INNER JOIN titles t
ON de.emp_no = t.emp_no AND de.to_date = '9999-01-01' AND t.to_date = '9999-01-01'
INNER JOIN departments dp ON dp.dept_no = de.dept_no
GROUP BY de.dept_no, t.title
```

