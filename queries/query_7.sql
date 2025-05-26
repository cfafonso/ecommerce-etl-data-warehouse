
-- Query 7:
-- Find the cities where customers who have placed at least 5 orders live, along with the total number
-- of orders placed by these customers by city.

  SELECT g.city, COUNT(*) AS num_orders
    FROM fact_order_header f
    JOIN dim_customer c
      ON f.customer_key = c.customer_key
    JOIN dim_geolocation g
      ON f.customer_geolocation_key = g.geolocation_key
   WHERE c.customer_unique_id IN (SELECT c2.customer_unique_id
                                    FROM dim_customer c2
                                    JOIN fact_order_header f2
                                      ON c2.customer_key = f2.customer_key
                                GROUP BY c2.customer_unique_id
                                  HAVING COUNT(*) >= 5)
GROUP BY g.city
ORDER BY num_orders DESC, city;