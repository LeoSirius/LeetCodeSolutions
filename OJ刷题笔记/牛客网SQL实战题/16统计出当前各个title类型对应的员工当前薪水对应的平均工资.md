题目描述

```

```

sql

```sql
SELECT t.title AS title, AVG(s.salary)
FROM salaries AS s INNER JOIN titles AS t
ON s.emp_no = t.emp_no AND s.to_date = '9999-01-01' AND t.to_date = '9999-01-01'
GROUP BY title
```

