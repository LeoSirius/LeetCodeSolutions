题目描述

```

```

sql

```sql
SELECT emp_no, COUNT(emp_no) AS t 
FROM salaries
GROUP BY emp_no HAVING t > 15;
```

