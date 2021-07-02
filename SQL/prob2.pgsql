







-- Создайте БД programmers.
-- Добавьте таблицу students:
-- id - Уникальный номер записи.
-- name - Имя студента
-- age - Возраст студента
-- fp_language - Основной Язык программирования
-- sp_language - Второй Язык программирования
-- В таблицу students, добавить записи:
-- id| name  | age| fp_language | sp_language
-- 1 | Bakyt | 23 | Python      | С++
-- 2 | Aygul | 46 | Python      | Java
-- 3 | Jika  | 13 | C           | Ruby_On_Rails
-- 4 | Ermek | 16 | Java        | C
-- 5 | Artem | 55 | C#          | Java
-- 6 | Roma  | 31 | Pascal      | C
-- 7 | Beka  | 25 | C#          | JavaScript

-- Напишите запрос, который выводит все имена студентов и языки программирования.
-- Напишите запрос, который выводит возраст студентов которым больше 30.
-- Выведите на экран всех студентов которые знают только Python или C#.
-- Выведите на экран всех студентов которые знают Python и C# или C# и Java.
-- Удалите всех студентов id которых равен 1, 3, 5, 7.
-- Узнайте самого молодого студента который знает Java.
-- Удалите таблицу students.
-- Удалите БД programmers. 

postgres=# CREATE DATABASE programmers;
CREATE DATABASE
postgres=# \c programmers;
You are now connected to database "programmers" as user "postgres".
programmers=# CREATE TABLE students(id SERIAL PRIMARY KEY, name VARCHAR, age VARCHAR, fp_language VARCHAR, sp_language VARCHAR);
CREATE TABLE
programmers=# \d
               List of relations
 Schema |      Name       |   Type   |  Owner   
--------+-----------------+----------+----------
 public | students        | table    | postgres
 public | students_id_seq | sequence | postgres
(2 rows)

programmers=# SELECT * FROM students;
 id | name | age | fp_language | sp_language 
----+------+-----+-------------+-------------
(0 rows)

programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Bakyt', 23, 'Python', 'C++');
INSERT 0 1
programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Aygul', 46, 'Python', 'Java');
INSERT 0 1
programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Jika', 13, 'C', 'Ruby_On_Rails');
INSERT 0 1
programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Ermek', 16, 'Java', 'C');
INSERT 0 1
programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Artem', 55, 'C#', 'Java');
INSERT 0 1
programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Roma', 31, 'Pascal', 'C');
INSERT 0 1
programmers=# INSERT INTO students(name, age, fp_language, sp_language) VALUES ('Beka', 25, 'C#', 'JavaScript');
INSERT 0 1

programmers=# SELECT * FROM students;
 id | name  | age | fp_language |  sp_language  
----+-------+-----+-------------+---------------
  1 | Bakyt | 23  | Python      | C++
  2 | Aygul | 46  | Python      | Java
  3 | Jika  | 13  | C           | Ruby_On_Rails
  4 | Ermek | 16  | Java        | C
  5 | Artem | 55  | C#          | Java
  6 | Roma  | 31  | Pascal      | C
  7 | Beka  | 25  | C#          | JavaScript
(7 rows)

-- Напишите запрос, который выводит все имена студентов и языки программирования.
programmers=# SELECT name, fp_language, sp_language FROM students;
 name  | fp_language |  sp_language  
-------+-------------+---------------
 Bakyt | Python      | C++
 Aygul | Python      | Java
 Jika  | C           | Ruby_On_Rails
 Ermek | Java        | C
 Artem | C#          | Java
 Roma  | Pascal      | C
 Beka  | C#          | JavaScript
(7 rows)


-- Напишите запрос, который выводит возраст студентов которым больше 30.
programmers=# ALTER TABLE students ALTER COLUMN age TYPE integer USING (trim(age)::integer);
ALTER TABLE
programmers=# SELECT age FROM students WHERE age > 30;
 age 
-----
  46
  55
  31
(3 rows)

--Выведите на экран всех студентов которые знают только Python или C#.
programmers=# SELECT name FROM students WHERE fp_language = 'Python' or fp_language = 'C' or sp_language = 'Python' or sp_language = 'C';
 name  
-------
 Bakyt
 Aygul
 Jika
 Ermek
 Roma
(5 rows)

--Выведите на экран всех студентов которые знают Python и C# или C# и Java.



-- Удалите всех студентов id которых равен 1, 3, 5, 7
programmers=# SELECT * FROM students;
 id | name  | age | fp_language |  sp_language  
----+-------+-----+-------------+---------------
  1 | Bakyt |  23 | Python      | C++
  2 | Aygul |  46 | Python      | Java
  3 | Jika  |  13 | C           | Ruby_On_Rails
  4 | Ermek |  16 | Java        | C
  5 | Artem |  55 | C#          | Java
  6 | Roma  |  31 | Pascal      | C
  7 | Beka  |  25 | C#          | JavaScript
(7 rows)

programmers=# DELETE FROM students WHERE id = 1 or id = 3 or id = 5 or id = 7;
DELETE 4

programmers=# SELECT * FROM students;
 id | name  | age | fp_language | sp_language 
----+-------+-----+-------------+-------------
  2 | Aygul |  46 | Python      | Java
  4 | Ermek |  16 | Java        | C
  6 | Roma  |  31 | Pascal      | C
(3 rows)

--Узнайте самого молодого студента который знает Java.
programmers=# SELECT * FROM students WHERE  or fp_language = 'Java' and sp_language = 'Java';
 name  
-------
 Ermek
(1 row)

-- Удалите таблицу students.
programmers=# DROP TABLE students;
DROP TABLE

-- Удалите БД programmers. 

postgres=# DROP DATABASE programmers;
DROP DATABASE

SELECT * FROM students WHERE age= (SELECT MIN(age) FROM students);