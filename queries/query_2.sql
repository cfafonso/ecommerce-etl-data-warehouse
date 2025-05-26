
-- Query 2:
-- What are the top 5 cities where customers who placed the most orders during the summer of 2017 live
-- and how many of such orders were placed?

  SELECT city, COUNT(*) AS num_placed_orders
    FROM dim_geolocation g
    JOIN (SELECT customer_geolocation_key
 		        FROM fact_order_header
	         WHERE purchase_date_key IN (SELECT date_key
								                         FROM dim_date
								                        WHERE full_date BETWEEN '2017-06-21' AND '2017-09-22')
                                      ) c
      ON c.customer_geolocation_key = g.geolocation_key
GROUP BY city
ORDER BY num_placed_orders DESC
LIMIT 5;