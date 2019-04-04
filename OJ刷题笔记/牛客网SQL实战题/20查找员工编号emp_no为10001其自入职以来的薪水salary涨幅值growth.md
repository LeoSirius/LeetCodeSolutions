题目描述

```

```

sql

```sql
SELECT 
(SELECT salary FROM salaries WHERE emp_no = 10001 ORDER BY to_date DESC LIMIT 1) - 
(SELECT salary FROM salaries WHERE emp_no = 10001 ORDER BY to_date ASC LIMIT 1)
AS growth
```

