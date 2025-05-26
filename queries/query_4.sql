
-- Query 4:
-- What is the average delivery time for products in each state?

  SELECT state, ROUND(AVG(delivery_time),0) AS average_delivery_time
    FROM dim_geolocation g
    JOIN fact_order_line f
      ON g.geolocation_key = f.customer_geolocation_key
GROUP BY state
ORDER BY average_delivery_time;