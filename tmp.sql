select p.project_id,round(avg(e.experience_years),2) average_years from
Project p left join Employee e on 
 p.employee_id=e.employee_id
group by project_id
order by project_id


CREATE TABLE `Weather` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `RecordDate` datetime(6) NOT NULL,
  `Temperature` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

INSERT INTO Weather VALUES 
(1, "2015-01-01", 10), (2, 2015-01-02, 25), (3, 2015-01-03, 20), (4, 2015-01-04, 30);


SELECT name, population, area
FROM World
WHERE area >= 3000000 or population >= 25000000;


SELECT name
FROM customers
WHERE referee_id != 2;

CREATE TABLE `Customers` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE `Orders` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `CustomerId` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;


CREATE TABLE `Employee` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(50) NOT NULL,
  `supervisor` int(50),
  `salary` int(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE `Employee` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Salary` int(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE `cinema` (
  `seat_id` int(11) NOT NULL AUTO_INCREMENT,
  `free` int(50) NOT NULL,
  PRIMARY KEY (`seat_id`)
) ENGINE=InnoDB;

INSERT INTO cinema VALUES
(1,1),(2,0),(3,1),(4,1),(5,1);

INSERT INTO Employee VALUES
(1, "John", 3, 1000),
(2, "Dan", 3, 2000),
(3, "Brad", null, 4000),
(4, "Thomas", 3, 4000);

CREATE TABLE `Bonus` (
  `Id` int(11) NOT NULL,
  `bonus` int(50) NOT NULL,
  PRIMARY KEY (`Id`, `bonus`)
) ENGINE=InnoDB;

INSERT INTO Bonus VALUES
(2, 500),
(4, 2000);

CREATE TABLE `Person` (
  `Id` int(11) NOT NULL,
  `Email` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

INSERT INTO Person VALUES (1, "john@example.com"), (2, "bob@example.com"), (3, "john@example.com");

SELECT Name
FROM Customers LEFT JOIN Orders
ON Customers.Id=Orders.CustomerId
WHERE Orders.CustomerId IS NULL;

SELECT Score, (
    SELECT COUNT(DISTINCT Score)
    FROM Scores
    WHERE Score >= s.Score) AS Rank
FROM Scores s
ORDER BY Score DESC;




CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary LIMIT M, 1
  );
END

select round(
  sum(case when datediff(a.event_date,b.first_date)=1 then 1 else 0 end)
  /
  (select count(distinct(player_id)) from activity), 2
  )
as fraction
from activity a,
(select player_id,min(event_date) first_date from activity group by player_id) b
where a.player_id=b.player_id;

SELECT ROUND(
  SUM(CASE WHEN DATEDIFF(a.event_date, b.first_date)=1 THEN 1 ELSE 0 END) / 
  (SELECT COUNT(DISTINCT(player_id)) FROM Activity)
  , 2
) AS fraction
FROM Activity a INNER JOIN
(SELECT player_id, MIN(event_date) first_date FROM Activity GROUP BY player_id) b
ON a.player_id=b.player_id;


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

CREATE TABLE `Weather` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `RecordDate` DATE NOT NULL,
  `Temperature` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

INSERT INTO Weather (Id, RecordDate, Temperature)
VALUES
(1,"2015-01-01", 10),
(2,"2015-01-02", 25),
(3,"2015-01-03", 20),
(4,"2015-01-04", 30);

CREATE TABLE `Activity` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) NOT NULL,
  `device_id` int(11) NOT NULL,
  `event_date` DATE NOT NULL,
  `games_played` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

INSERT INTO Activity VALUES 
  (1,1,2,"2016-03-01",5),
  (2,1,2,"2016-05-02",6),
  (3,2,3,"2017-06-25",1),
  (4,3,1,"2016-03-02",0),
  (5,3,4,"2018-07-03",5);

INSERT INTO Activity VALUES 
(1,1,2,"2016-03-01",5),
(2,1,2,"2016-05-02",6),
(3,1,3,"2015-06-25",1),
(4,3,1,"2016-03-02",0),
(5,3,4,"2016-02-03",5);


CREATE TABLE `Employee2` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Company` char(50) NOT NULL,
  `Salary` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

INSERT INTO Employee2 VALUES
(1, "A", 2341),
(2, "A", 341),
(3, "A", 15),
(4, "A", 15341),
(5, "A", 451),
(6, "A", 513),
(7, "B", 15),
(8, "B", 13),
(9, "B", 1154),
(10, "B", 1345),
(11, "B", 1221),
(12, "B", 234),
(13, "C", 2345),
(14, "C", 2645),
(15, "C", 2645),
(16, "C", 2652),
(17, "C", 65);

SELECT
    Employee2.Id, Employee2.Company, Employee2.Salary
FROM
    Employee2,
    Employee2 alias
WHERE
    Employee2.Company = alias.Company
GROUP BY Employee2.Company, Employee2.Salary;


CREATE TABLE `courses` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `student` char(50) NOT NULL,
  `class` char(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE `Product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` char(50) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB;

INSERT INTO Product VALUES
(1, "G8"),
(2, "G4"),
(3, "iphone");

CREATE TABLE `Submissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_id` int(11) NOT NULL,
  `parent_id` int(11),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

INSERT INTO Submissions VALUES
(1, 1, NULL),
(2, 2, NULL),
(3, 1, NULL),
(4, 12, NULL),
(5, 3, 1),
(6, 5, 2),
(7, 3, 1),
(8, 4, 1),
(9, 9, 1),
(10, 10, 2),
(11, 6, 7);

CREATE TABLE `Sales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `sale_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

INSERT INTO Sales VALUES
(1, 1, "2019-01-21"),
(2, 2, "2019-02-17"),
(3, 2, "2019-06-02"),
(4, 3, "2019-05-13");

CREATE TABLE `Employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB;

INSERT INTO Employee VALUES
(1,8),
(2,8),
(3,8),
(4,7),
(5,9),
(6,9);

INSERT INTO courses VALUES
(1, "A", "Math"),
(2, "B", "English"),
(3, "C", "Math"),
(4, "D", "Biology"),
(5, "E", "Math"),
(6, "F", "Computer"),
(8, "G", "Math"),
(9, "H", "Math"),
(10, "I", "Math");


| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
