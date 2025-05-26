
-- Query 5:
-- From sellers who have sold 500 or more products, how many products did they sell in each city?

SELECT city, COUNT(*) AS num_products_sold
  FROM dim_geolocation g
  JOIN (SELECT seller_geolocation_key
		      FROM fact_order_line
		     WHERE seller_key IN (SELECT seller_key
								                FROM fact_order_line
							              GROUP BY seller_key
						                  HAVING COUNT(*) >= 500)) f
	  ON g.geolocation_key = f.seller_geolocation_key
GROUP BY city
ORDER BY num_products_sold DESC;