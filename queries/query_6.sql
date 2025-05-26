
-- Query 6:
-- How many delivered orders with a review score of at least 3 have been paid by each payment type?

  SELECT payment_type, COUNT(*) AS num_delivered_orders
    FROM fact_order_header f
    JOIN dim_order_indicator o
      ON f.order_indicator_key = o.order_indicator_key
   WHERE review_score >= 3
     AND order_status = 'delivered'
GROUP BY payment_type
ORDER BY num_delivered_orders;