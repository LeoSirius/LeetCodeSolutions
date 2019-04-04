题目描述

```

```

sql

```sql
SELECT emp_no FROM employees 
WHERE emp_no NOT IN (SELECT emp_no FROM dept_manager);
```

