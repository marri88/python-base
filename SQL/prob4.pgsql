-- 1. Cоздайте БД kyrgyzstan
-- 2. Создайте таблицу developers(id, name, population):
-- 3. Добавьте Chuy, 100000
-- 4. Добавьте Osh, 200000
-- 5. Добавьте Naryn, 300000
-- 6. Добавьте колонку teams
-- 7. Переименуйте колонку population на participants
-- 8. Удалите записи где population равен 300000
-- 9. Так получилось что программа подсчёта участников сломалась и во всех
-- столбцах были добавлены лишние значения. Уменьшите количество
-- участников на 7000 везде где количество больше 80000.


-- 1. Cоздайте БД kyrgyzstan
postgres=# CREATE DATABASE kyrgyzstan;
CREATE DATABASE

-- 2. Создайте таблицу developers(id, name, population):
CREATE TABLE developers(id SERIAL PRIMARY KEY, name VARCHAR, population INTEGER);
CREATE TABLE

-- 3. Добавьте Chuy, 100000
INSERT INTO developers(name, population) VALUES ('Chui', 100000);
INSERT 0 1
-- 4. Добавьте Osh, 200000
INSERT INTO developers(name, population) VALUES ('Osh', 200000);
INSERT 0 1
-- 5. Добавьте Naryn, 300000
INSERT INTO developers(name, population) VALUES ('Naryn', 300000);
INSERT 0 1

-- 7. Переименуйте колонку population на participants
ALTER TABLE developers RENAME COLUMN population TO participants;
ALTER TABLE

-- 8. Удалите записи где population равен 300000
DELETE FROM developers WHERE participants = 300000;
DELETE 1

-- 9. Так получилось что программа подсчёта участников сломалась и во всех
-- столбцах были добавлены лишние значения. Уменьшите количество
-- участников на 7000 везде где количество больше 80000.
UPDATE developers SET participants = 7000 WHERE participants > 80000;
UPDATE 2

SELECT * FROM developers;
 id | name | participants 
----+------+--------------
  1 | Chui |         7000
  2 | Osh  |         7000
(2 rows)


