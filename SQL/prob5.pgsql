-- 1. Создайте БД  
-- 2. Создайте таблицу phons(id,name,price)
-- 3. Добавьте запись, IPhone, 100
-- 4. Добавьте колонку country
-- 5. Добавьте запись, Samsung, 120, korea
-- 6. Добавьте запись, Nokia, 1000, kyrgyzstan
-- 7. Добавьте запись, MI, 1, uzbekstan
-- 8. Добавьте запись, Google, free, USA
-- 9. Создайте таблицу cars(id,name, price DEFAULT 300
-- 10. Добавьте запись MB, 1000
-- 11. Добавьте колонку country
-- 12. Добавьте запись Audi, 300, Germany
-- 13. Добавьте запись BMW, 12000, Germany
-- 14. Добавьте запись Tulpar, 1000000, Kyrgyzstan
-- 15. Добавьте значение Germany в country для MB



-- 1. Создайте БД  
postgres=# CREATE DATABASE 
CREATE DATABASE

postgres=# \c u are now connected to database "s user "postgres".

-- 2. Создайте таблицу phons(id,name,price)
CREATE TABLE phons(id SERIAL PRIMARY KEY, name VARCHAR, price INTEGER);
CREATE TABLE
-- 3. Добавьте запись, IPhone, 100
INSERT INTO phons(name, price) VALUES ('IPhone', 100);
INSERT 0 1
-- 4. Добавьте колонку country
ALTER TABLE phons ADD COLUMN country VARCHAR;
ALTER TABLE
-- 5. Добавьте запись, Samsung, 120, korea
INSERT INTO phons(name, price, country) VALUES ('Samsung', 120, 'Korea');
INSERT 0 1
-- 6. Добавьте запись, Nokia, 1000, kyrgyzstan
INSERT INTO phons(name, price, country) VALUES ('Nokia', 120, 'Kyrgyzstan');
INSERT 0 1
-- 7. Добавьте запись, MI, 1, uzbekstan
INSERT INTO phons(name, price, country) VALUES ('MI', 1, 'Uzbekstan');
INSERT 0 1
--Добавьте запись, Google, free, USA
INSERT INTO phons(name, price, country) VALUES ('Google', 100, 'USA');
INSERT 0 1


SELECT * FROM phons;
 id |  name   | price |  country   
----+---------+-------+------------
  1 | IPhone  |   100 | 
  2 | Samsung |   120 | Korea
  3 | Nokia   |   120 | Kyrgyzstan
  4 | MI      |     1 | Uzbekstan
  5 | Google  |   100 | USA
(5 rows)


-- 9. Создайте таблицу cars(id,name, price DEFAULT 300
CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR, price INTEGER DEFAULT 300);
CREATE TABLE

-- 10. Добавьте запись MB, 1000
INSERT INTO cars(name, price) VALUES('MB', 1000);
INSERT 0 1

-- 11. Добавьте колонку country
ALTER TABLE cars ADD COLUMN country VARCHAR;
ALTER TABLE

-- 12. Добавьте запись Audi, 300, Germany
INSERT INTO cars(name, price, country) VALUES('Audi', 300, 'Germany');
INSERT 0 1
-- 13. Добавьте запись BMW, 12000, Germany
INSERT INTO cars(name, price, country) VALUES('BMW', 12000, 'Germany');
INSERT 0 1
-- 14. Добавьте запись Tulpar, 1000000, Kyrgyzstan
INSERT INTO cars(name, price, country) VALUES('Tulpar', 1000000, 'Kyrgyzstan');
INSERT 0 1
-- 15. Добавьте значение Germany в country для MB
UPDATE cars SET country = 'Germany' WHERE id = 4;
UPDATE 1

SELECT * FROM cars;
 id |  name  |  price  | country 
----+--------+---------+---------
  1 | Audi   |     300 | Germany
  2 | BMW    |   12000 | Germany
  3 | Tulpar | 1000000 | Germany
  4 | MB     |    1000 | Germany
(4 rows)






