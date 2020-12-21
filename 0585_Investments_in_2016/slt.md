### 思路1 利用子查询

criteria1: 15年的有多个  (在作为子查询时，必须用TIV_2015，如果用PID的话，只能筛选出这个组里的一个)

```sql
SELECT TIV_2015 
FROM insurance
GROUP BY TIV_2015
HAVING COUNT(*)>1;
```

criteria2: 地理位置重复

```sql
SELECT LAT, LON
FROM insurance
GROUP BY LAT, LON
HAVING COUNT(*)=1;
```

同时满足上面两个criteria即可

```sql
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
```