CREATE TABLE If Not Exists point_2d (x INT NOT NULL, y INT NOT NULL);
Truncate table point_2d;
insert into point_2d (x, y) values ('-1', '-1');
insert into point_2d (x, y) values ('0', '0');
insert into point_2d (x, y) values ('-1', '-2');


Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.
 

Write a query to find the shortest distance between these points rounded to 2 decimals.
 

| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |

注意这里的不等联结，一定要把多列括起来，不然判断的就是单列的不等

SELECT ROUND(
  MIN(SQRT(ABS(p2.y-p1.y)*ABS(p2.y-p1.y) + ABS(p2.x-p1.x)*ABS(p2.x-p1.x)))
  , 2)
AS shortest
FROM point_2d p1 JOIN point_2d p2
ON (p1.x, p1.y)!=(p2.x, p2.y);
 

The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
 

| shortest |
|----------|
| 1.00     |

