### 思路1 利用子查询

1. 找出有相同的2015

```sql
SELECT *
FROM insurance
GROUP BY TIV_2015
HAVING COUNT(TIV_2015)>1;
```

2. 找到有重复的地理位置

```sql
SELECT LAT, LON
FROM insurance
GROUP BY LAT, LON
HAVING COUNT(*)>1;
```

3. 找出所有的在1中的PID用户，但地理位置不在2中的用户。最后求SUM即可

```sql
SELECT ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM insurance
WHERE TIV_2015 IN(
  SELECT TIV_2015
  FROM insurance
  GROUP BY TIV_2015
  HAVING COUNT(TIV_2015)>1
)
AND
(LAT, LON) NOT IN (
  SELECT LAT, LON
  FROM insurance
  GROUP BY LAT, LON
  HAVING COUNT(*)>1
);
```
