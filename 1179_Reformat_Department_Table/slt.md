### 思路1

```sql
SELECT id,
SUM(CASE month WHEN "Jan" THEN revenue ELSE NULL END) AS Jan_Revenue,
SUM(CASE month WHEN "Feb" THEN revenue ELSE NULL END) AS Feb_Revenue,
SUM(CASE month WHEN "Mar" THEN revenue ELSE NULL END) AS Mar_Revenue,
SUM(CASE month WHEN "Apr" THEN revenue ELSE NULL END) AS Apr_Revenue,
SUM(CASE month WHEN "May" THEN revenue ELSE NULL END) AS May_Revenue,
SUM(CASE month WHEN "Jun" THEN revenue ELSE NULL END) AS Jun_Revenue,
SUM(CASE month WHEN "Jul" THEN revenue ELSE NULL END) AS Jul_Revenue,
SUM(CASE month WHEN "Aug" THEN revenue ELSE NULL END) AS Aug_Revenue,
SUM(CASE month WHEN "Sep" THEN revenue ELSE NULL END) AS Sep_Revenue,
SUM(CASE month WHEN "Oct" THEN revenue ELSE NULL END) AS Oct_Revenue,
SUM(CASE month WHEN "Nov" THEN revenue ELSE NULL END) AS Nov_Revenue,
SUM(CASE month WHEN "Dec" THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department
GROUP BY id;
```
