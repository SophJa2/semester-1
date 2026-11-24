.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- 1. List every column for every driver.
-- .schema drivers


--2. List the name and price of every dish sold by Bangkok Garden (restaurant 3).
-- select name,price from menu_items where restaurant_id = '3';

-- 3. List the names of all the Indian restaurants.
-- SELECT name FROM restaurants WHERE cuisine = 'Indian';

-- 4. How many customers does Leeds Eats have?
-- select count(*) from customers;

-- silver

-- 5. select name,price from menu_items where price <= 8;

-- 6. select name,hygiene_rating from restaurants where hygiene_rating < 4 ;

-- 7. select name, postcode, hygiene_rating from restaurants where postcode LIKE 'LS6%' order by hygiene_rating desc;

-- 8. **The marketing team:** "We want to email everyone who signed up with a University of Leeds email address, newest members first." Write the query, then say whether Leeds Eats should actually send this email.
-- select email, name,joined_date from customers order by joined_date

-- 9. **The operations manager:** "Show me the 10 most recent cancelled orders."
select order_id,order_time from orders where status = 'cancelled' order by order_time limit 10

-- 10. **The owner of Pasta Pronto (restaurant 4):** "Which of my dishes are vegetarian? And what's my most expensive dish?" (Two queries.)

