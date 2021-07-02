CREATE TABLE product_types(
    product_type_id SERIAL PRIMARY KEY, 
    product_type_name VARCHAR(30)
);
CREATE TABLE globus (
    product_id SERIAL PRIMARY KEY,
    product_type_id SMALLINT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_amount INT NOT NULL,
    day_to_expire SMALLINT NOT NULL,
    date_delivered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_type
    FOREIGN KEY (product_type_id)
    REFERENCES product_types(product_type_id)
);
CREATE TABLE narodnii (
    product_id SERIAL PRIMARY KEY,
    product_type_id SMALLINT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_amount INT NOT NULL,
    day_to_expire SMALLINT NOT NULL,
    date_delivered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_type
    FOREIGN KEY (product_type_id)
    REFERENCES product_types(product_type_id)
);
INSERT INTO product_types (product_type_name) VALUES ('Molochnoe');
INSERT INTO product_types (product_type_name) VALUES ('Vipechka');
INSERT INTO product_types (product_type_name) VALUES ('Shokolad');
INSERT INTO narodnii (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Snikers', 600, 2021-04-15);
INSERT INTO narodnii (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Twix', 1000, 2021-06-25);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Yashkino', 90, 2021-04-13);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Nutella', 23, 2021-04-15);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Alpen Gold', 555, 2021-07-12);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Bounty', 45, 2021-05-24);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Airan', 60, 2021-04-17);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kaimak', 10, 2021-07-09);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Moloko', 49, 2021-04-23);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kumis', 15, 2021-06-30);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Shoro', 55, 2021-04-12);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Cheese', 5, 2021-04-09);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Yougurt', 65, 2021-04-28);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Hleb', 60, 2021-04-26);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Bulochki', 10, 2021-03-28);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pizza', 49, 2021-06-15);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Boorsoki', 15, 2021-04-16);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pirojki', 55, 2021-05-17);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Chebureki', 5, 2021-04-25);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Cakes', 65, 2021-04-26);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Bounty', 213, 2021-04-15);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Alpen Gold', 503, 2021-12-25);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Nutella', 24, 2021-04-06);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Yashkino', 903, 2021-04-05);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Kit Kat', 113, 2021-05-14);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Twix', 763, 2021-06-17);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Snikers', 223, 2021-05-06);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Airan', 446, 2021-05-23);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kaimak', 657, 2021-04-23);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Moloko', 23, 2021-07-13);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kumis', 713, 2021-04-15);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Shoro', 21, 2021-04-08);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Cheese', 441, 2021-06-17);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Yougurt', 845, 2021-07-29);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Hleb', 204, 2021-06-20);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Bulochki', 21, 2021-04-16);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pizza', 13, 2021-05-20);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Boorsoki', 23, 2021-07-15);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pirojki', 73, 2021-04-25);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Chebureki', 923, 2021-05-19);
INSERT INTO globus (product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Cakes', 123, 2021-03-05);
