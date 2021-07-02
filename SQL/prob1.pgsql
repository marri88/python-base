


-- Создайте БД tourist;
-- Внутри БД создайте 2 ТАБЛИЦЫ:
-- inner_flights
-- outter_flights
-- В таблице inner_flights должны хранится такие поля как:
-- id - уникальный идентификатор каждой записи
-- from_region - Регион Вылета
-- to_destination - Регион Прилёта
-- company - Компания которая занимается перевозкой
-- quantity - Количество человек летящее этим рейсом
-- В таблице outter_flights должны быть такие поля как:
-- id - уникальный идентификатор каждой записи
-- from_country - Страна вылета
-- to_country - Страна прилёта
-- flight_type - Грузовой или Пассажирский
-- company - Компания которая занимается перевозкой
-- neighbors - Количество стран через которые самолёт будет пролетать.

-- Создайте по 15 записей в каждой таблице с разными значениями.

-- Из таблицы inner_flights выведите все записи.

-- Из таблицы inner_flights выведите только те строки где id больше 10.
-- Из таблицы inner_flights выведите только те строки где страна прилёта Ош или Бишкек.
-- Из таблицы inner_flights выведите только те строки где количество пассажиров больше 150.

-- Из таблицы outter_flights выведите только имена компаний которые занимаются перевозкой.
-- Из таблицы outter_flights выведите только те строки где id меньше 7.
-- Из таблицы outter_flights выведите только те строки где тип рейса грузовой.
-- Из таблицы outter_flights выведите только те строки где самолёт пролетает больше чем над 3 странами.
-- Из таблицы outter_flights выведите только те строки где самолёт пролетает меньше чем над 3 странами И тип рейса пассажирский.
-- Из таблицы outter_flights выведите только имена всех компаний и страны прилёта.


tourist=# CREATE TABLE inner_flights(id SERIAL PRIMARY KEY,
from_region VARCHAR,
to_destination VARCHAR,
company VARCHAR,
quantity INTEGER);
CREATE TABLE
tourist=# \d
                  List of relations
 Schema |         Name         |   Type   |  Owner   
--------+----------------------+----------+----------
 public | inner_flights        | table    | postgres
 public | inner_flights_id_seq | sequence | postgres
(2 rows)

tourist=# CREATE TABLE outter_flights(id SERIAL PRIMARY KEY,
from_country VARCHAR,
to_country VARCHAR,
flight_type VARCHAR,
company VARCHAR,
neighbors INTEGER);
CREATE TABLE
tourist=# \d
                  List of relations
 Schema |         Name          |   Type   |  Owner   
--------+-----------------------+----------+----------
 public | inner_flights         | table    | postgres
 public | inner_flights_id_seq  | sequence | postgres
 public | outter_flights        | table    | postgres
 public | outter_flights_id_seq | sequence | postgres
(4 rows)

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 clients   | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
 clients1  | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
 postgres  | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
 template0 | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 tourist   | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
(6 rows)


-- Создайте по 15 записей в каждой таблице с разными значениями.--

postgres=# \c tourist;
You are now connected to database "tourist" as user "postgres".
tourist=# \d
                  List of relations
 Schema |         Name          |   Type   |  Owner   
--------+-----------------------+----------+----------
 public | inner_flights         | table    | postgres
 public | inner_flights_id_seq  | sequence | postgres
 public | outter_flights        | table    | postgres
 public | outter_flights_id_seq | sequence | postgres
(4 rows)


tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 1);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 2);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 3);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 4);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 5);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 6);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 7);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 8);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 9);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 10);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 11);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 12);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 13);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 14);
INSERT 0 1
tourist=# INSERT INTO inner_flights(from_region, to_destination, company, quantity) VALUES ('bishkek', 'astana', 'air', 15);
INSERT 0 1

tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 1);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 2);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 3);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 4);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 5);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 6);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 7);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 8);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 9);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 10);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 11);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 12);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 13);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 14);
INSERT 0 1
tourist=# INSERT INTO outter_flights(from_country, to_country, flight_type, company, neighbors) VALUES ('bishkek', 'astana', 'pass', 'air', 15);
INSERT 0 1


--Из таблицы inner_flights выведите все записи.--

tourist=# \d
                  List of relations
 Schema |         Name          |   Type   |  Owner   
--------+-----------------------+----------+----------
 public | inner_flights         | table    | postgres
 public | inner_flights_id_seq  | sequence | postgres
 public | outter_flights        | table    | postgres
 public | outter_flights_id_seq | sequence | postgres
(4 rows)

tourist=# SELECT * FROM inner_flights;
 id | from_region | to_destination | company | quantity 
----+-------------+----------------+---------+----------
  1 | bishkek     | astana         | air     |        1
  2 | bishkek     | astana         | air     |        2
  3 | bishkek     | astana         | air     |        3
  4 | bishkek     | astana         | air     |        4
  5 | bishkek     | astana         | air     |        5
  6 | bishkek     | astana         | air     |        6
  7 | bishkek     | astana         | air     |        7
  8 | bishkek     | astana         | air     |        8
  9 | bishkek     | astana         | air     |        9
 10 | bishkek     | astana         | air     |       10
 11 | bishkek     | astana         | air     |       11
 12 | bishkek     | astana         | air     |       12
 13 | bishkek     | astana         | air     |       13
 14 | bishkek     | astana         | air     |       14
 15 | bishkek     | astana         | air     |       15
(15 rows)


--Из таблицы outter_flights выведите все записи.--

tourist=# \d
                  List of relations
 Schema |         Name          |   Type   |  Owner   
--------+-----------------------+----------+----------
 public | inner_flights         | table    | postgres
 public | inner_flights_id_seq  | sequence | postgres
 public | outter_flights        | table    | postgres
 public | outter_flights_id_seq | sequence | postgres
(4 rows)

tourist=# SELECT * FROM outter_flights;
 id | from_country | to_country | flight_type | company | neighbors 
----+--------------+------------+-------------+---------+-----------
  1 | bishkek      | astana     | pass        | air     |         1
  2 | bishkek      | astana     | pass        | air     |         2
  3 | bishkek      | astana     | pass        | air     |         3
  4 | bishkek      | astana     | pass        | air     |         4
  5 | bishkek      | astana     | pass        | air     |         5
  6 | bishkek      | astana     | pass        | air     |         6
  7 | bishkek      | astana     | pass        | air     |         7
  8 | bishkek      | astana     | pass        | air     |         8
  9 | bishkek      | astana     | pass        | air     |         9
 10 | bishkek      | astana     | pass        | air     |        10
 11 | bishkek      | astana     | pass        | air     |        11
 12 | bishkek      | astana     | pass        | air     |        12
 13 | bishkek      | astana     | pass        | air     |        13
 14 | bishkek      | astana     | pass        | air     |        14
 15 | bishkek      | astana     | pass        | air     |        15
(15 rows)

--Из таблицы inner_flights выведите только те строки где id больше 10--

tourist=# SELECT * FROM inner_flights WHERE id > 10;
 id | from_region | to_destination | company | quantity 
----+-------------+----------------+---------+----------
 11 | bishkek     | astana         | air     |       11
 12 | bishkek     | astana         | air     |       12
 13 | bishkek     | astana         | air     |       13
 14 | bishkek     | astana         | air     |       14
 15 | bishkek     | astana         | air     |       15
(5 rows)

--Из таблицы inner_flights выведите только те строки где страна прилёта Ош или Бишкек.--
tourist=# SELECT to_destination FROM inner_flights WHERE to_destination = 'bishkek' or to_destination = 'osh';
 to_destination 
----------------
(0 rows)

--Из таблицы inner_flights выведите только те строки где количество пассажиров больше 150.--
tourist=# SELECT quantity FROM inner_flights WHERE quantity > 150;
 quantity 
----------
(0 rows)

--Из таблицы outter_flights выведите только имена компаний которые занимаются перевозкой--
tourist=# SELECT company FROM outter_flights;
 company 
---------
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
(15 rows)

-- Из таблицы outter_flights выведите только те строки где id меньше 7--
tourist=# SELECT * FROM outter_flights WHERE id < 7;
 id | from_country | to_country | flight_type | company | neighbors 
----+--------------+------------+-------------+---------+-----------
  1 | bishkek      | astana     | pass        | air     |         1
  2 | bishkek      | astana     | pass        | air     |         2
  3 | bishkek      | astana     | pass        | air     |         3
  4 | bishkek      | astana     | pass        | air     |         4
  5 | bishkek      | astana     | pass        | air     |         5
  6 | bishkek      | astana     | pass        | air     |         6
(6 rows)

-- Из таблицы outter_flights выведите только те строки где тип рейса грузовой.--
tourist=# SELECT flight_type  FROM outter_flights WHERE flight_type = 'gruz';
 flight_type 
-------------
(0 rows)

-- Из таблицы outter_flights выведите только те строки где самолёт пролетает больше чем над 3 странами.--
tourist=# SELECT neighbors FROM outter_flights WHERE neighbors > 3;
 neighbors 
-----------
         4
         5
         6
         7
         8
         9
        10
        11
        12
        13
        14
        15
(12 rows)

--Из таблицы outter_flights выведите только те строки где самолёт пролетает меньше чем над 3 странами И тип рейса пассажирский.--
tourist=# SELECT neighbors FROM outter_flights WHERE neighbors > 3; SELECT flight_type  FROM outter_flights WHERE flight_type = 'pass';
 neighbors 
-----------
         4
         5
         6
         7
         8
         9
        10
        11
        12
        13
        14
        15
(12 rows)

 flight_type 
-------------
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
 pass
(15 rows)

-- Из таблицы outter_flights выведите только имена всех компаний и страны прилёта.--
tourist=# SELECT company FROM outter_flights; SELECT to_country FROM outter_flights;
 company 
---------
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
 air
(15 rows)

 to_country 
------------
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
 astana
(15 rows)

