题目描述

```

```

sql

```sql
SELECT f.film_id, f.title 
FROM film as f LEFT JOIN film_category as fc
ON f.film_id = fc.film_id
WHERE fc.category_id IS NULL
```

