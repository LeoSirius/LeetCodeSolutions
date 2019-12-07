### 思路1

GROUP BY + COUNT + LIMIT

```sql
SELECT customer_number
FROM orders 
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;
```