# Write your MySQL query statement below
SELECT name FROM SalesPerson
WHERE sales_id NOT IN 
(SELECT o.sales_id 
 FROM Orders o LEFT JOIN Company c ON o.com_id = c.com_id
 WHERE name = 'RED');