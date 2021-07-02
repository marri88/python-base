-- 1. Найдите сколько разных типов продуктов в таблице globus.
market=# SELECT count(*) FROM product_types;
 count 
-------
     3
(1 row)


-- 2. Используя HAVING найдите сколько и каких продуктов в narodnii испортятся меньше
-- чем через 2 дня.

market=# SELECT product_name,day_to_expire FROM narodnii WHERE day_to_expire BETWEEN '1990' AND '2000';
 product_name | day_to_expire 
--------------+---------------
 Twix         |          1990
 Bounty       |          1992
 Airan        |          2000
 Moloko       |          1994
 Hleb         |          1991
 Bulochki     |          1990
 Pizza        |          2000
 Pirojki      |          1999
 Chebureki    |          1992
 Cakes        |          1991
(10 rows)



-- 3. Посчитайте в каком магазине больше сникерсов в globus или narodnii.
SELECT * FROM globus FULL OUTER JOIN narodnii ON globus.product_name = narodnii.product_name WHERE globus.product_name = 'Snikers' AND narodnii.product_name = 'Snikers';


-- 4. Посмотрите продукты в globus и narodnii у которых product_type равен сроку
-- годности продукта

-- 5. Посмотрите продукты из globus и narodnii у которых одинаковый срок годности.
SELECT * FROM globus FULL OUTER JOIN narodnii ON globus.day_to_expire = narodnii.day_to_expire WHERE globus.day_to_expire = '1999' AND narodnii.day_to_expire = '1999';

\
-- 6. Через Python подключитесь к БД main и узнайте сколько ВСЕГО piyaz в магазине
-- globus.
-- 7. Через Python удалите из магазина narodnii все продукты у которых срок годности 0.
-- 8. Если ПРОДУКТ и СРОК ГОДНОСТИ продукта одинаковы в globus и narodnii удалите эту
-- запись из globus.
-- 9. Напишите запрос, который выводит всю информацию продукта из народного,
-- где количество продуктов 200 < продукт < 1001
-- 10. Напишите запрос, который соединяет таблицы глобус народный
-- и выводит day delivered
-- 11. Напишите запрос, который соединяет таблицы глобус народный
-- по столбцу глобуса и выводит название продукта
-- 12. Напишите запрос, который соединяет таблицы глобус народный
-- по столбцу народного и выводит название продукта
-- 13. Напишите запрос, который соединяет таблицы глобус народный
-- по столбцу глобуса и выводит название продукта
-- 14. Напишите запрос, который соединяет таблицы глобус народный
-- и выводит совпадения количества продуктов.
-- 15. Напишите запрос, который выводит продукты глобуса,
-- где название заканчивается на a, b, c, d, e, f, g, a


postgres=# CREATE DATABASE market;
CREATE DATABASE
postgres=# \c market
You are now connected to database "market" as user "postgres".
market=#
market=# \i /home/aimira/main.pgsql
CREATE TABLE
CREATE TABLE
CREATE TABLE

