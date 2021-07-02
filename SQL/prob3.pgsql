-- 1. Создайте БД department
-- 2. Создайте таблицу developers(id,name,skill,programming_lang по умолчанию установите
-- значение HTML):
-- 3. Переименуйте колонку skill на age.
-- 4. В таблицу developers, добавить запись:
-- 5. Добавить 'Bakyt', 23, 'Python'
-- 6. Добавить Beka, 15 лет Java
-- 7. Добавьте Gulya, 30 лет, JavaScript
-- 8. Добавьте Beka, 39 лет, Assembler
-- 9. Добавьте к уже существующей таблице developers столбец cash.
-- 10. Добавьте запись Katya, 16, Python, 3000
-- 11. Поменяйте значение возраста на 27 тех пользователей, возразраст которых больше 25.
-- 12. Добавьте комментарий 'Имя пользователя' к столбцу name.
-- 13. Измените все записи Katya в колонке name на Ekaterina.

\l
                                  List of databases
    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
------------+----------+----------+-------------+-------------+-----------------------
 department | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
 postgres   | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
 template0  | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | =c/postgres          +
            |          |          |             |             | postgres=CTc/postgres
 template1  | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | =c/postgres          +
            |          |          |             |             | postgres=CTc/postgres
 tourist    | postgres | UTF8     | ru_RU.UTF-8 | ru_RU.UTF-8 | 
(5 rows)


-- 1. Создайте БД department
\c department;
You are now connected to database "department" as user "postgres".

-- 2. Создайте таблицу developers(id,name,skill,programming_lang по умолчанию установите
-- значение HTML)
CREATE TABLE developers(id SERIAL PRIMARY KEY, name VARCHAR, skill VARCHAR, programming_lang VARCHAR DEFAULT 'HTML');
CREATE TABLE

-- 3. Переименуйте колонку skill на age.
ALTER TABLE developers RENAME COLUMN skill TO age;
ALTER TABLE

-- 4. В таблицу developers, добавить запись:
ALTER TABLE developers ALTER COLUMN age TYPE integer USING (trim(age)::integer);
ALTER TABLE
SELECT * FROM developers;
 id | name | age | programming_lang 
----+------+-----+------------------
(0 rows)

-- 4. В таблицу developers, добавить запись:
-- 5. Добавить 'Bakyt', 23, 'Python'
-- 6. Добавить Beka, 15 лет Java
-- 7. Добавьте Gulya, 30 лет, JavaScript
-- 8. Добавьте Beka, 39 лет, Assembler
INSERT INTO developers(name, age, programming_lang)VALUES('Bakyt', 23, 'Python');
INSERT 0 1
INSERT INTO developers(name, age, programming_lang)VALUES('Beka', 15,'Java');
INSERT 0 1
INSERT INTO developers(name, age, programming_lang)VALUES('Gulya', 30, 'JavaScript');
INSERT 0 1
INSERT INTO developers(name, age, programming_lang)VALUES('Beka', 39, 'Assembler');

-- 9. Добавьте к уже существующей таблице developers столбец cash.
ALTER TABLE developers ADD COLUMN cash INTEGER;
ALTER TABLE
SELECT * FROM developers;
 id | name  | age | programming_lang | cash 
----+-------+-----+------------------+------
  1 | Bakyt |  23 | Python           |     
  2 | Beka  |  15 | Java             |     
  3 | Gulya |  30 | JavaScript       |     
  4 | Beka  |  39 | Assembler        |     
(4 rows)

-- 10. Добавьте запись Katya, 16, Python, 3000
INSERT INTO developers(name, age, programming_lang, cash)VALUES('Katya', 16, 'Python', 3000);
INSERT 0 1
SELECT * FROM developers;
 id | name  | age | programming_lang | cash 
----+-------+-----+------------------+------
  1 | Bakyt |  23 | Python           |     
  2 | Beka  |  15 | Java             |     
  3 | Gulya |  30 | JavaScript       |     
  4 | Beka  |  39 | Assembler        |     
  5 | Katya |  16 | Python           | 3000
(5 rows)

-- 11. Поменяйте значение возраста на 27 тех пользователей, возразраст которых больше 25.
UPDATE developers SET cash = 27 WHERE age < 25;
UPDATE 3
SELECT * FROM developers;
 id | name  | age | programming_lang | cash 
----+-------+-----+------------------+------
  3 | Gulya |  30 | JavaScript       |     
  4 | Beka  |  39 | Assembler        |     
  1 | Bakyt |  23 | Python           |   27
  2 | Beka  |  15 | Java             |   27
  5 | Katya |  16 | Python           |   27
(5 rows)

-- 12. Добавьте комментарий 'Имя пользователя' к столбцу name.
COMMENT ON COLUMN developers.name is '<Имя Пользователя>';
COMMENT

-- 13. Измените все записи Katya в колонке name на Ekaterina.
UPDATE developers SET name = 'Ekaterina' WHERE name = 'Katya';
UPDATE 1
SELECT * FROM developers;
 id |   name    | age | programming_lang | cash 
----+-----------+-----+------------------+------
  3 | Gulya     |  30 | JavaScript       |     
  4 | Beka      |  39 | Assembler        |     
  1 | Bakyt     |  23 | Python           |   27
  2 | Beka      |  15 | Java             |   27
  5 | Ekaterina |  16 | Python           |   27
(5 rows)