
-- Query 1:
-- What are the categories of the 10 most sold products during the first trimester of 2017?

  SELECT category
    FROM dim_product p
    JOIN (SELECT product_key, COUNT(*)
            FROM fact_order_line
           WHERE purchase_date_key IN (SELECT date_key
                                         FROM dim_date
                                        WHERE year = 2017
                                          AND trimester = 'Q1')
	      GROUP BY product_key
	      ORDER BY count DESC
           LIMIT 10) f
      ON p.product_key = f.product_key
GROUP BY category;