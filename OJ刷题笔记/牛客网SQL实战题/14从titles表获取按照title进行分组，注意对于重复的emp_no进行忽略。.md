题目描述

```

```

sql

```sql
SELECT title, COUNT(DISTINCT emp_no) AS t
FROM titles
GROUP BY title HAVING t >= 2;
```

