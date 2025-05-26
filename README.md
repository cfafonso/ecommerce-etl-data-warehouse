# ecommerce-etl-data-warehouse
This project implements an ETL (Extract, Transform, Load) pipeline in Python to create an ecommerce data warehouse in PostgreSQL, with business intelligence reporting through SQL querying and PowerBI dashboards. The data for this project is from the [Olist e-commerce transaction dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), which is divided into multiple csv files, each containing data pertaining to the operational activities of the store.


## Specification of the Project

### Data Warehouse

#### 1. OrderLine

This fact table is connected to five dimension tables (customer, seller, product, geolocation, date). It has a finer grain where each row corresponds to a unique line item within a customer order and contains the complete transaction lifecycle: the specific product purchased, the customer who bought it, the seller who fulfilled it, origin and delivery locations, and all relevant timestamps including purchase, approval, and final delivery dates. The schema for this fact table and dimensions can be found within the `schemas` folder.

#### 2. OrderHeader

This fact table is connected to four dimension tables (customer, geolocation, date, order indicator). It has a coarser grain where each row corresponds to a unique order placed by a customer, delivered at a particular location and characterized by purchase, approval and delivery dates. The schema for this fact table and dimensions can be found within the `schemas` folder.


## Prerequisites

- Python 3.x
- PostgreSQL
- pgAdmin
- PowerBI


## Installation

### 1. Download or clone the repository

```git clone https://github.com/cfafonso/ecommerce-etl-pipeline.git```


### 2. Install the required packages:

```pip install -r requirements.txt```


### 3. Download the dataset files.

Option 1: 
- Run the `00_dataset_download.py` file to programatically download the [Olist e-commerce transaction dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) CSV files. This option requires configuring the Kaggle API first.


Option 2:

- Go to the [Olist e-commerce transaction dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and manually download the CSV files. Place the downloaded files within the `data/original_datasets` folder.


### 4. Ensure PostgreSQL is running on your system.

- Set the password for the PostgreSQL database superuser (postgres) in the `constants.py` file.


### 5. Usage

- Run the following Jupyter notebooks sequentially:

```
01_data_analysis_processing.ipynb
02_create_dimensions.ipynb
03_create_facts.ipynb
04_load_dimensions.ipynb
05_load_facts.ipynb
```


Alternatively, the first three Jupyter notebooks can be bypassed since the dimension and fact tables (as CSV files) resulting from the Extract and Transform steps of the ETL process can be found within the ```data/dimension_tables``` and ```data/fact_tables``` folders, respectively.


#### Run the queries in pgAdmin

Several SQL queries were made and these can be found in within the `queries` folder. The SQL files can be run independently in pgAdmin.

- Query 1 - What are the categories of the 10 most sold products during the first trimester of 2017?

- Query 2 - What are the top 5 cities where customers who placed the most orders during the summer of 2017 live and how many of such orders were placed?

- Query 3 - What is the average product price in each category?

- Query 4 - What is the average delivery time for products in each state?

- Query 5 - From sellers who have sold 500 or more products, how many products did they sell in each city?

- Query 6 - How many delivered orders with a review score of at least 3 have been paid by each payment type?

- Query 7 - Find the cities where customers who have placed at least 5 orders live, along with the total number of orders placed by these customers by city.

- Query 8 - Find the unique customer identifiers that have never left any review score below 5 and who have made at least one purchase in January 2017.


#### Visualize the PowerBI dashboards to answer three analytical questions

- Question 1 - Which states spent the most money on orders, for each trimester between 2016-18?

To visualize the report that answers question 1, see the `order_header_fact_table.pbix` file.

- Question 2 - Over time, what are the differences in delivery times (from order approval to delivery to the customer) between metropolitan and regional areas?

- Question 3 - Is there any temporal variation in the product categories sold in Olist?

To visualize the report that answers questions 2 and 3, see the `order_line_fact_table.pbix` file.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Structure

```
ecommerce-etl-data-warehouse
├── data/
    ├── dimension_tables/
        ├── dim_customer_geolocation.csv
        ├── dim_customer.csv
        ├── dim_date.csv
        ├── dim_geolocation.csv
        ├── dim_order_indicator.csv
        ├── dim_product.csv
        ├── dim_seller_geolocation.csv
        └── dim_seller.csv
    ├── fact_tables/
        ├── fact_order_header.csv
        └── fact_order_line.csv
    ├── lookup_tables/
        ├── lut_customer_geolocation.json
        ├── lut_customer.json
        ├── lut_date.json
        ├── lut_geolocation.json
        ├── lut_order_indicator.json
        ├── lut_order_number.json
        ├── lut_product.json
        ├── lut_seller_geolocation.json
        └── lut_seller.json
    ├── original_datasets/
        ├── olist_customers_dataset.csv
        ├── olist_geolocation_dataset.csv
        ├── olist_order_items_dataset.csv
        ├── olist_order_payments_dataset.csv
        ├── olist_order_reviews_dataset.csv
        ├── olist_orders_dataset.csv
        ├── olist_products_dataset.csv
        ├── olist_sellers_dataset.csv
        └── product_category_name_translation.csv
    └── processed_datasets/
        ├── category.csv
        ├── customers.csv
        ├── geolocation.csv
        ├── items.csv
        ├── orders.csv
        ├── payments.csv
        ├── products.csv
        ├── reviews.csv
        └── sellers.csv
├── plots/
    ├── number_products_per_category.png
    ├── product_height_by_category.png
    ├── product_length_by_category.png
    ├── product_weight_by_category.png
    └── product_width_by_category.png
├── queries/
    ├── query_1.sql
    ├── query_2.sql
    ├── query_3.sql
    ├── query_4.sql
    ├── query_5.sql
    ├── query_6.sql
    ├── query_7.sql
    └── query_8.sql
├── reports/
    ├── order_header_fact_table.pbix
    └── order_line_fact_table.pbix
├── schemas/
    ├── star_schema_order_header_accumulating_fact_table.png
    └── star_schema_order_line_accumulating_fact_table.png
├── utils/
    ├── constants.py
    ├── data_comparison.py
    ├── data_warehouse_mappings.py
    ├── dates.py
    └── plots.py
├── LICENSE
├── README.md
├── 00_dataset_download.py
├── 01_data_processing.ipynb
├── 02_create_dimensions.ipynb
├── 03_create_facts.ipynb
├── 04_load_dimensions.ipynb
├── 05_load_facts.ipynb
└── requirements.txt
