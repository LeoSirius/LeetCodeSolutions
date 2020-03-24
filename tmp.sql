CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT Salary FROM Employee ORDER BY Salary LIMIT (N-1), 1
  );
END