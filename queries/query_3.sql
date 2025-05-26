
-- Query 3:
-- What is the average product price in each category?

  SELECT category, ROUND(AVG(average_product_price),2) AS average_category_price
    FROM dim_product p
    JOIN (SELECT product_key, AVG(unit_price) AS average_product_price
		        FROM fact_order_line
	      GROUP BY product_key) f
	    ON p.product_key = f.product_key
GROUP BY category
ORDER BY average_category_price DESC;