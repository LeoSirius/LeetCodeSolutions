### 思路1

使用case when和month

```sql
SELECT c.country_name,
    CASE 
        WHEN AVG(weather_state) <= 15 THEN "Cold"
        WHEN AVG(weather_state) >= 25 THEN "Hot"
        ELSE "Warm"
    END weather_type
FROM Countries c JOIN Weather w
ON c.country_id=w.country_id
WHERE MONTH(w.day)=11
GROUP BY c.country_id;
```
