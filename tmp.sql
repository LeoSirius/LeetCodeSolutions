Create table If Not Exists Employee (employee_id int, team_id int);
Truncate table Employee;
insert into Employee (employee_id, team_id) values ('1', '8');
insert into Employee (employee_id, team_id) values ('2', '8');
insert into Employee (employee_id, team_id) values ('3', '8');
insert into Employee (employee_id, team_id) values ('4', '7');
insert into Employee (employee_id, team_id) values ('5', '9');
insert into Employee (employee_id, team_id) values ('6', '9');

Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
Result table:
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+

SELECT  e1.employee_id,
COUNT(*) AS team_size
FROM Employee e1 JOIN Employee e2
ON e1.team_id=e2.team_id
GROUP BY e1.employee_id;