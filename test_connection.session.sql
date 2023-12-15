DROP TABLE Users;
DROP TABLE products;

CREATE TABLE Users (
  user_id INT AUTO_INCREMENT PRIMARY KEY ,
  username VARCHAR(50)
);
CREATE TABLE Products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(255),
  price DECIMAL(10 , 2)
);

INSERT INTO Products (product_name, price) VALUES ('Widget A', 19.99);
INSERT INTO Products (product_name, price) VALUES ('Widget B', 29.99);
INSERT INTO Products (product_name, price) VALUES ('Widget C', 26.99);


UPDATE Products SET price = 24.99 WHERE product_id = 1;
DELETE FROM Products WHERE product_id = 2;


SELECT * FROM Products
