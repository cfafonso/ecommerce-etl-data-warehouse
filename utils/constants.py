
# This file records the constants used in the ecommerce-etl-data-warehouse project

# PostgreSQL
host = 'localhost'
user = 'postgres'
password = 1234
database_name = 'ecommerce_warehouse'

# Folder names
original_dataset_folder = './data/original_datasets/'
processed_dataset_folder = './data/processed_datasets/'
dimension_tables_folder = './data/dimension_tables/'
fact_tables_folder = './data/fact_tables/'
lookup_tables_folder = './data/lookup_tables/'
plots_folder = './plots/'

# File names
## Original datasets
customers_original_dataset = 'olist_customers_dataset.csv'
geolocation_original_dataset = 'olist_geolocation_dataset.csv'
items_original_dataset = 'olist_order_items_dataset.csv'
payments_original_dataset = 'olist_order_payments_dataset.csv'
reviews_original_dataset = 'olist_order_reviews_dataset.csv'
orders_original_dataset = 'olist_orders_dataset.csv'
products_original_dataset = 'olist_products_dataset.csv'
sellers_original_dataset = 'olist_sellers_dataset.csv'
category_original_dataset = 'product_category_name_translation.csv'

## Processed datasets
customers_processed_dataset = 'customers.csv'
geolocation_processed_dataset = 'geolocation.csv'
items_processed_dataset = 'items.csv'
payments_processed_dataset = 'paymentrs.csv'
reviews_processed_dataset = 'reviews.csv'
orders_processed_dataset = 'orders.csv'
products_processed_dataset = 'products.csv'
sellers_processed_dataset = 'sellers.csv'
category_processed_dataset = 'category.csv'

## Dimension tables
dim_customer_file = 'dim_customer.csv'
dim_seller_file = 'dim_seller.csv'
dim_product_file = 'dim_product.csv'
dim_geolocation_file = 'dim_geolocation.csv'
dim_customer_geolocation_file = 'dim_customer_geolocation.csv'
dim_seller_geolocation_file = 'dim_seller_geolocation.csv'
dim_order_indicator_file = 'dim_order_indicator.csv'
dim_date_file = 'dim_date.csv'

## Fact tables
fact_order_line_file = 'fact_order_line.csv'
fact_order_header_file = 'fact_order_header.csv'

## Lookup tables
lookup_table_customer = 'lut_customer.json'
lookup_table_seller = 'lut_seller.json'
lookup_table_product = 'lut_product.json'
lookup_table_geolocation = 'lut_geolocation.json'
lookup_table_customer_geolocation = 'lut_customer_geolocation.json'
lookup_table_seller_geolocation = 'lut_seller_geolocation.json'
lookup_table_order_indicator = 'lut_order_indicator.json'
lookup_table_date = 'lut_date.json'
lookup_table_order_number = 'lut_order_number.json'

# Mappings
## Maps the abbreviated state names to their respective full names 
state_mappings = {'SP': 'São Paulo',
                  'RJ': 'Rio de Janeiro',
                  'ES': 'Espírito Santo',
                  'MG': 'Minas Gerais',
                  'BA': 'Bahia',
                  'SE': 'Sergipe',
                  'PE': 'Pernambuco',
                  'RN': 'Rio Grande do Norte',
                  'AL': 'Alagoas',
                  'PB': 'Paraíba',
                  'CE': 'Ceará',
                  'PI': 'Piauí',
                  'MA': 'Maranhão',
                  'PA': 'Pará',
                  'AP': 'Amapá',
                  'AM': 'Amazonas',
                  'RR': 'Roraima',
                  'AC': 'Acre',
                  'DF': 'Distrito Federal',
                  'GO': 'Goiás',
                  'RO': 'Rondônia',
                  'TO': 'Tocantins',
                  'MT': 'Mato Grosso',
                  'MS': 'Mato Grosso do Sul',
                  'PR': 'Paraná',
                  'SC': 'Santa Catarina',
                  'RS': 'Rio Grande do Sul'}

## Maps the category names in portuguese to their respective english terms
category_mappings = {'perfumaria': 'Health and Beauty',
                     'artes': 'Music and Art',
                     'esporte_lazer' : 'Sports and Leisure',
                     'bebes': 'Children',
                     'utilidades_domesticas' : 'Home and Decor',
                     'instrumentos_musicais': 'Music and Art', 
                     'cool_stuff': 'Others',
                     'moveis_decoracao': 'Home and Decor' , 
                     'eletrodomesticos': 'Technology and Home Appliances', 
                     'brinquedos':'Children' ,
                     'cama_mesa_banho': 'Home and Decor', 
                     'construcao_ferramentas_seguranca' : 'Materials and Construction',
                     'informatica_acessorios': 'Technology and Home Appliances', 
                     'beleza_saude': 'Health and Beauty', 
                     'malas_acessorios': 'Fashion',
                     'ferramentas_jardim': 'Materials and Construction', 
                     'moveis_escritorio': 'Home and Decor', 
                     'automotivo': 'Others',
                     'eletronicos': 'Technology and Home Appliances', 
                     'fashion_calcados': 'Fashion', 
                     'telefonia': 'Technology and Home Appliances', 
                     'papelaria': 'Stationery and Books',
                     'fashion_bolsas_e_acessorios': 'Fashion', 
                     'pcs': 'Technology and Home Appliances', 
                     'casa_construcao': 'Materials and Construction',
                     'relogios_presentes': 'Fashion', 
                     'construcao_ferramentas_construcao': 'Materials and Construction',
                     'pet_shop': 'Animals', 
                     'eletroportateis': 'Technology and Home Appliances', 
                     'agro_industria_e_comercio': 'Services and Commerce', 
                     'moveis_sala': 'Home and Decor', 
                     'sinalizacao_e_seguranca': 'Materials and Construction', 
                     'climatizacao': 'Technology and Home Appliances',
                     'consoles_games': 'Technology and Home Appliances', 
                     'livros_interesse_geral': 'Stationery and Books',
                     'construcao_ferramentas_ferramentas': 'Materials and Construction',
                     'fashion_underwear_e_moda_praia': 'Fashion', 
                     'fashion_roupa_masculina': 'Fashion',
                     'moveis_cozinha_area_de_servico_jantar_e_jardim': 'Home and Decor' ,
                     'industria_comercio_e_negocios': 'Services and Commerce', 
                     'telefonia_fixa': 'Technology and Home Appliances',
                     'construcao_ferramentas_iluminacao': 'Materials and Construction', 
                     'livros_tecnicos': 'Stationery and Books',
                     'eletrodomesticos_2': 'Technology and Home Appliances', 
                     'artigos_de_festas': 'Home and Decor', 
                     'bebidas': 'Food',
                     'market_place': 'Market Place', 
                     'la_cuisine': 'Home and Decor', 
                     'construcao_ferramentas_jardim': 'Materials and Construction',
                     'fashion_roupa_feminina': 'Fashion', 
                     'casa_conforto': 'Home and Decor', 
                     'audio': 'Technology and Home Appliances',
                     'alimentos_bebidas':'Food', 
                     'musica': 'Music and Art', 
                     'alimentos': 'Food',
                     'tablets_impressao_imagem': 'Technology and Home Appliances', 
                     'livros_importados': 'Stationery and Books',
                     'portateis_casa_forno_e_cafe': 'Technology and Home Appliances', 
                     'fashion_esporte': 'Fashion',
                     'artigos_de_natal': 'Home and Decor', 
                     'fashion_roupa_infanto_juvenil': 'Fashion',
                     'dvds_blu_ray': 'Music and Art' , 
                     'artes_e_artesanato': 'Music and Art', 
                     'pc_gamer': 'Technology and Home Appliances', 
                     'moveis_quarto':'Home and Decor',
                     'cine_foto':'Music and Art' , 
                     'fraldas_higiene': 'Children', 
                     'flores':'Home and Decor', 
                     'casa_conforto_2':'Home and Decor',
                     'portateis_cozinha_e_preparadores_de_alimentos': 'Technology and Home Appliances',
                     'seguros_e_servicos': 'Services and Commerce', 
                     'moveis_colchao_e_estofado':'Home and Decor',
                     'cds_dvds_musicais':'Music and Art',
                     'sem categoria':'Without Category'}