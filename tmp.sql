Write a query to print the sum of all total investment values in 2016 (TIV_2016), to a scale of 2 decimal places, for all policy holders who meet the following criteria:

Have the same TIV_2015 value as one or more other policyholders.

Are not located in the same city as any other policyholder
 (i.e.: the (latitude, longitude) attribute pairs must be unique).
Input Format:
The insurance table is described as follows:

| Column Name | Type          |
|-------------|---------------|
| PID         | INTEGER(11)   |
| TIV_2015    | NUMERIC(15,2) |
| TIV_2016    | NUMERIC(15,2) |
| LAT         | NUMERIC(5,2)  |
| LON         | NUMERIC(5,2)  |
where PID is the policyholder's' policy ID, TIV_2015 is the total investment value in 2015, TIV_2016 is the total investment value in 2016, LAT is the latitude of the policy holder's city, and LON is the longitude of the policy holder's city.

Sample Input

| PID | TIV_2015 | TIV_2016 | LAT | LON |
|-----|----------|----------|-----|-----|
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |

criteria1: 15年的有多个

SELECT TIV_2015 
FROM insurance
GROUP BY TIV_2015
HAVING COUNT(*)>1;

criteria2: 地理位置重复

SELECT LAT, LON
FROM insurance
GROUP BY LAT, LON
HAVING COUNT(*)=1;

同时满足上面两个criteria即可

SELECT ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM insurance
WHERE TIV_2015 IN (
    SELECT TIV_2015
    FROM insurance
    GROUP BY TIV_2015
    HAVING COUNT(*)>1
) AND (LAT, LON) IN (
    SELECT LAT, LON
    FROM insurance
    GROUP BY LAT, LON
    HAVING COUNT(*)=1
);

SELECT ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM insurance
WHERE PID IN (
    SELECT TIV_2015
    FROM insurance
    GROUP BY TIV_2015
    HAVING COUNT(*)>1
) AND (LAT, LON) NOT IN (
    SELECT LAT, LON
    FROM insurance
    GROUP BY LAT, LON
    HAVING COUNT(*)>1
);


    SELECT PID
    FROM insurance
    GROUP BY LAT, LON
    HAVING COUNT(*)>1;



+------+----------+----------+-------+-------+
| PID  | TIV_2015 | TIV_2016 | LAT   | LON   |
+------+----------+----------+-------+-------+
|    1 |   224.17 |   952.73 | 32.40 | 20.20 |
|    2 |   224.17 |   900.66 | 52.40 | 32.70 |
|    3 |   824.61 |   645.13 | 72.40 | 45.20 |
|    4 |   424.32 |   323.66 | 12.40 |  7.70 |
|    5 |   424.32 |   282.90 | 12.40 |  7.70 |
|    6 |   625.05 |   243.53 | 52.50 | 32.80 |
|    7 |   424.32 |   968.94 | 72.50 | 45.30 |
|    8 |   624.46 |   714.13 | 12.50 |  7.80 |
|    9 |   425.49 |   463.85 | 32.50 | 20.30 |
|   10 |   624.46 |   776.85 | 12.40 |  7.70 |
|   11 |   624.46 |   692.71 | 72.50 | 45.30 |
|   12 |   225.93 |   933.00 | 12.50 |  7.80 |
|   13 |   824.61 |   786.86 | 32.60 | 20.30 |
|   14 |   824.61 |   935.34 | 52.60 | 32.80 |
+------+----------+----------+-------+-------+
1: 1348

+------+
|    1 |
|    9 |
|   13 |
|    2 |
|    6 |
|   14 |
|    3 |
+------+

Sample Output

| TIV_2016 |
|----------|
| 45.00    |


CREATE TABLE IF NOT EXISTS insurance (PID INTEGER(11), TIV_2015 NUMERIC(15,2), TIV_2016 NUMERIC(15,2), LAT NUMERIC(5,2), LON NUMERIC(5,2) );
Truncate table insurance;
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('1', '10', '5', '10', '10');
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('2', '20', '20', '20', '20');
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('3', '10', '30', '20', '20');
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('4', '10', '40', '40', '40');

insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (2,224.17,900.66,52.4,32.7);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (1,224.17,952.73,32.4,20.2);


{"headers":{"insurance":["PID","TIV_2015","TIV_2016","LAT","LON"]},

insert into insurance values (1,224.17,952.73,32.4,20.2);
insert into insurance values (2,224.17,900.66,52.4,32.7);
insert into insurance values (3,824.61,645.13,72.4,45.2);
insert into insurance values (4,424.32,323.66,12.4,7.7);
insert into insurance values (5,424.32,282.9,12.4,7.7);
insert into insurance values (6,625.05,243.53,52.5,32.8);
insert into insurance values (7,424.32,968.94,72.5,45.3);
insert into insurance values (8,624.46,714.13,12.5,7.8);
insert into insurance values (9,425.49,463.85,32.5,20.3);
insert into insurance values (10,624.46,776.85,12.4,7.7);
insert into insurance values (11,624.46,692.71,72.5,45.3);
insert into insurance values (12,225.93,933,12.5,7.8);
insert into insurance values (13,824.61,786.86,32.6,20.3);
insert into insurance values (14,824.61,935.34,52.6,32.8);