The Employee table holds all employees. Every employee has an Id, a salary, 
and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in 
each of the departments. For the above tables, your SQL query should 
return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

SELECT *
FROM Employee e JOIN

(
SELECT d.Id MAX(e.Salary) AS Salary
FROM Employee e JOIN Department d
ON e.DepartmentId=d.Id
GROUP BY d.Id) AS t
ON e.DepartmentId=t.Id;

SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM Employee e JOIN Department d
ON e.DepartmentId=d.Id
WHERE (e.Salary, e.DepartmentId) IN
(
SELECT MAX(Salary) AS Salary, DepartmentId
FROM Employee
GROUP BY DepartmentId);

Explanation:

Max and Jim both have the highest salary in the IT department and 
Henry has the highest salary in the Sales department.


Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
Create table If Not Exists Department (Id int, Name varchar(255));

insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Jim', '90000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'Max', '90000', '1');

insert into Department (Id, Name) values ('1', 'IT');
insert into Department (Id, Name) values ('2', 'Sales');