
-- Query 8: Find the unique customer identifiers that have never left any review score
-- below 5 and who have made at least one purchase in January 2017

(SELECT DISTINCT c.customer_unique_id
   FROM dim_customer c
   JOIN fact_order_header f
     ON c.customer_key = f.customer_key
  WHERE NOT EXISTS (SELECT *
                      FROM fact_order_header f2
                     WHERE f2.customer_key = c.customer_key
                       AND f2.review_score < 5))
INTERSECT
(SELECT DISTINCT c1.customer_unique_id
   FROM dim_customer c1
  WHERE EXISTS (SELECT *
                  FROM fact_order_header f3
                  JOIN dim_date d
                    ON f3.purchase_date_key = d.date_key
                 WHERE f3.customer_key = c1.customer_key
                   AND d.month = 1
                   AND d.year = 2017))