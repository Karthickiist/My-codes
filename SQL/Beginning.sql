USE sales;

CREATE TABLE sales (
    purchase_number INT NOT NULL AUTO_INCREMENT,
    date_of_purchase DATE NOT NULL,
    Customer_id INT,
    Item_code VARCHAR(10) NOT NULL,
    PRIMARY KEY (purchase_number)
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints INT,
    PRIMARY KEY (customer_id)
);

CREATE TABLE items (
    item_code VARCHAR(255),
    item VARCHAR(255),
    unit_price NUMERIC(10 , 2 ),
    company_id VARCHAR(255),
    PRIMARY KEY (item_code)
);

CREATE TABLE companies (
    company_id VARCHAR(255),
    company_name VARCHAR(255),
    headquarters_phone_number INT(12),
    PRIMARY KEY (company_id)
);

alter table customers
add column gender enum('M','F') after last_name;

INSERT INTO customers (first_name, last_name, gender, email_address, number_of_complaints)

VALUES ('John', 'Mackinley', 'M', 'john.mckinley@365careers.com', 0);

alter table companies
add unique key(headquarters_phone_number);


