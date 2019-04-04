题目描述

```

```

sql

```sql
SELECT se.emp_no as emp_no, sm.emp_no as manager_no, se.salary as emp_salary, sm.salary as manager_salary
FROM
(SELECT s.emp_no, s.salary, de.dept_no 
FROM salaries s INNER JOIN dept_emp de 
ON s.emp_no = de.emp_no AND s.to_date = '9999-01-01') as se,
(SELECT s.emp_no, s.salary, dm.dept_no 
FROM salaries s INNER JOIN dept_manager dm 
ON s.emp_no = dm.emp_no AND s.to_date = '9999-01-01') as sm
WHERE se.dept_no = sm.dept_no AND se.salary > sm.salary
```

