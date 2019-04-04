题目描述

```

```

sql

```sql
SELECT title, COUNT(title) AS t 
FROM titles 
GROUP BY title HAVING t >= 2;
```

