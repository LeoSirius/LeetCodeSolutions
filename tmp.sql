select d.name as Department,e.name as Employee,e.salary as Salary 
from Employee as e inner join Department as d on e.DepartmentId=d.id 
where (select count( distinct salary) 
      from Employee 
      where salary>e.salary and departmentid=e.DepartmentId )<3 
order by e.departmentid,Salary desc;


SELECT d.name as Department, e.name AS Employee, e.salary as Salary
FROM Employee as e inner join Department as d
ON e.DepartmentId=d.Id
WHERE (
  SELECT count(distinct Salary)
  FROM Employee
  WHERE Salary > e.Salary AND DepartmentId=e.DepartmentId
)<3
ORDER BY e.DepartmentId, e.Salary DESC;



CREATE TABLE `Employee`

CREATE TABLE `Employee` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(50) NOT NULL,
  `Salary` int(50) NOT NULL,
  `DepartmentId` int(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE `Department` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;


INSERT INTO Employee (Id, Name, Salary, DepartmentId) 
Values
(2, "Henry", 80000, 2),
(3, "Sam", 60000, 2),
(4, "Max", 90000, 1),
(5, "Janet", 69000, 1),
(6, "Randy", 85000, 1),
(7, "Will", 70000, 1);

INSERT INTO Department VALUES (1, "IT"), (2, "Sales");
