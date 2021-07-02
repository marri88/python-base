-- 1. Посчитайте количество записей
-- 2. Сколько followerОВ у самого знаменитого пользователя
-- 3. Напишите запрос, который выводит всю информацию самого знаменитого пользователя
-- 4. Найдите среднее количество подписчиков
-- 5. Отсортируйте всех пользователей по логину
-- 6. Отсортируйте всех пользователей по стране
-- 7. Отсортируйте всех пользователей по email
-- 8. Напишите запрос,который выводит id из колонки пользователей и имя из колонки clients
-- 9. Напишите запрос,который выводит всё о пользователе, чей логин содержит as, cg, si, am, qwe, er, ka, an
-- 10. Напишите запрос,который выводит всё о пользователе, чей логин заканчивается на lol, kan, ck, ie. ig
-- 11. Напишите запрос, который выводит всё о пользователе, чей логин начинается на a, b, c, d, M, D, A
-- 12. 12.Как зовут самого знаменитого Сеньор Программиста(Senior Programmer) из Израиля(Israel)?


-- 1. Выведите на экран всех пользователей у кого пустая почта.
-- 2. Посчитайте сколько пользователей у которых нет email живут на Chui.
-- 3. Покажите имена и номера телефонов всех людей которые работают как Web Developer
-- 4. У всех пользователей у которых почта ровняется False обновите почту на user@gmail.com.
-- 5. Узнайте из каких стран люди которые не имею работы(Unemployed).
-- 6. Везде где номер телефона начинается с 000 замените его любой РЕАЛЬНЫЙ номер в формате
-- столбца phone_number.
-- 7. 12345, user123б, qwerty считается лёгкими паролями у каждого пользователя у кого лёгкий
-- пароль удалите из Базы Данных.
-- 8. Выведите на экран email всех .NET Developer разработчиков и отсортируйте их по Имени.


 CREATE DATABASE instagram;
CREATE DATABASE
 \c instagram
You are now connected to database "instagram" as user "postgres".
\i /home/aimira/part4.sql
CREATE TABLE

-- 1. Посчитайте количество записей
SELECT count(*) FROM part4;
 count 
-------
  1000
(1 row)

-- 2. Сколько followerОВ у самого знаменитого пользователя
SELECT max(followers) FROM part4;
  max   
--------
 998294
(1 row)

-- 3. Напишите запрос, который выводит всю информацию самого знаменитого пользователя
SELECT * FROM part4 WHERE followers = (SELECT MAX(followers) FROM part4);
 id  | first_name | last_name  | followers |     users     |  country  |         email          |   profession    
-----+------------+------------+-----------+---------------+-----------+------------------------+-----------------
 923 | Pascale    | Greensides |    998294 | pgreensidespm | Indonesia | pgreensidespm@ebay.com | Cost Accountant
(1 row)

-- 4. Найдите среднее количество подписчиков
SELECT AVG(followers) FROM part4;
         avg         
---------------------
 505291.650000000000
(1 row)

-- 5. Отсортируйте всех пользователей по логину
SELECT users FROM part4 ORDER BY users;

-- 6. Отсортируйте всех пользователей по стране
SELECT country FROM part4 ORDER BY country;

-- 7. Отсортируйте всех пользователей по email
SELECT email FROM part4 ORDER BY email;

-- 8. Напишите запрос,который выводит id из колонки пользователей и имя из колонки clients
\i /home/aimira/part42.sql;
CREATE TABLE

SELECT clients FROM part42
SELECT id,clients FROM part42;

-- 9. Напишите запрос,который выводит всё о пользователе, чей логин содержит as, cg, si, am, qwe, er, ka, an
SELECT * FROM part42 WHERE users LIKE '%as%'OR users LIKE '%cg%'OR users LIKE '%si%'OR users LIKE '%am%' OR users  LIKE '%qwe%' OR users LIKE '%er% 'OR users LIKE '%ka%' OR users LIKE '%an%';

-- 10. Напишите запрос,который выводит всё о пользователе, чей логин заканчивается на lol, kan, ck, ie. ig
SELECT * FROM part42 WHERE users LIKE '%lol'OR users LIKE '%kan'OR users LIKE '%ck'OR users LIKE '%ie' OR users  LIKE '%ig';

-- 11. Напишите запрос, который выводит всё о пользователе, чей логин начинается на a, b, c, d, M, D, A
SELECT * FROM part42 WHERE users LIKE 'a%'OR users LIKE 'b%'OR users LIKE 'c%'OR users LIKE 'd%' OR users  LIKE 'M%' OR users  LIKE 'D%' OR users  LIKE 'A%';

 -- 12. 12.Как зовут самого знаменитого Сеньор Программиста(Senior Programmer) из Израиля(Israel)?
 SELECT *  FROM part42 WHERE profession = 'Senior Editor' AND country = 'Israel';
 id  | first_name | last_name | followers |   users   | country |        email         | password  |  profession   |     clients     | phone_number  
-----+------------+-----------+-----------+-----------+---------+----------------------+-----------+---------------+-----------------+---------------
 544 | Waverley   | McClay    |    312826 | wmcclayf3 | Israel  | wmcclayf3@sphinn.com | aQeoMh1e5 | Senior Editor | Waverley McClay | (836) 4897151
(1 row)



-- 1. Выведите на экран всех пользователей у кого пустая почта
SELECT * FROM part42 WHERE email IS NULL;

-- 2. Посчитайте сколько пользователей у которых нет email живут на Canada.
SELECT * FROM part42 WHERE email IS NULL and country = 'Canada';
 id  | first_name | last_name | followers |    users    | country | email |   password   |     profession      |    clients     | phone_number  
-----+------------+-----------+-----------+-------------+---------+-------+--------------+---------------------+----------------+---------------
 785 | Dale       | Unger     |    834526 | dungerls    | Canada  |       | Fzl1rRZ      |                     | Dale Unger     | (630) 4405739
 805 | Mirilla    | Stoke     |    839893 | mstokemc    | Canada  |       | NhXy9RaK     | Social Worker       | Mirilla Stoke  | (976) 1865941
 808 | Herb       | Bletcher  |    587731 | hbletchermf | Canada  |       | I6PPzDhA2    | Associate Professor | Herb Bletcher  | (412) 2047207
 826 | Wells      | Woodison  |    774311 | wwoodisonmx | Canada  |       | rZy3ms698H7M | Engineer IV         | Wells Woodison | (466) 3898125
 913 | Wallas     | Lucas     |     80846 | wlucaspc    | Canada  |       | dlRjgmY      | Financial Advisor   | Wallas Lucas   | (460) 9159925
(5 rows)


-- 3. Покажите имена и номера телефонов всех людей которые работают как Senior Editor
SELECT clients, phone_number FROM part42 WHERE profession = 'Senior Editor';
     clients      | phone_number  
------------------+---------------
 Abdel Tayloe     | (843) 4687047
 Lenci Campelli   | (334) 7328584
 Damita Duchateau | (952) 6786958
 Kenna Whitfield  | (812) 6185833
 Waverley McClay  | (836) 4897151
 Renato Lardge    | (284) 9019491
 Izak Frome       | (600) 9569762
 Hedda Westoff    | (808) 9246364
 Winfield Selwin  | (540) 7713995
(9 rows)


-- 4. У всех пользователей у которых почта ровняется False обновите почту на user@gmail.com.
UPDATE part42 SET email = 'user@gmail.com' WHERE email = 'False' ;
UPDATE 0

-- 5. Узнайте из каких стран люди которые не имею работы(Unemployed).
--ver 1
SELECT clients, country FROM part42 WHERE profession IS NULL;
--ver 2
SELECT clients, country FROM part42 WHERE profession = 'Unemployed';
SELECT clients, country FROM part42 WHERE profession = 'Unemployed';
 clients | country 
---------+---------
(0 rows)

-- 6. Везде где номер телефона начинается с 000 замените его любой РЕАЛЬНЫЙ номер в формате столбца phone_number.
UPDATE part42 SET phone_number = '(996)999699026' WHERE phone_number LIKE '(160)%';
UPDATE 2

-- 7. 12345, user123б, qwerty считается лёгкими паролями у каждого пользователя у кого лёгкий пароль удалите из Базы Данных.(этих значений нету, поэтому пишем другие)
DELETE FROM part42  WHERE password = 'VDLKIa' OR password = 'ShdqfK' OR password = 'JdejS9g';
DELETE 3

-- 8. Выведите на экран email всех .NET Developer разработчиков и отсортируйте их по Имени. (Senior Editor)

SELECT email FROM part42 WHERE profession = 'Senior Editor' ORDER BY clients;
SELECT * FROM part42 WHERE profession = 'Senior Editor' ORDER BY clients;
