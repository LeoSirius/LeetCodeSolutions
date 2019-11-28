SELECT Email
FROM Person
GROUP BY Email
HAVING Count(Email) > 1;