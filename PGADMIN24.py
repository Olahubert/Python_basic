
import psycopg2
pgconn = psycopg2.connect(
host = "localhost",
user = "postgres",
password = "Olawale",
database= "ecommerce_db")

pgcursor = pgconn.cursor()

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
pgconn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# ("ALTER user 'postgres' WITH 'password' 'Ayomikun19'")

# pgcursor.execute("CREATE DATABASE mydatabase")

# # pgcursor.execute("CREATE TABLE street(name VARCHAR(255))")
# sqlformular = "INSERT INTO street (name)  VALUES (%s)"
# # pgcursor.execute(sqlformular)
# my_list=[("Coka","Dicson","Badmus","Surulere")]
# for x in my_list:
#     pgcursor.execute(sqlformular, x)

# pgcursor.execute("CREATE DATABASE ecommerce_db")
# pgcursor.execute("CREATE TABLE customers(customer_id INTEGER,name VARCHAR(255),email VARCHAR (255),city VARCHAR (255))")

pgcursor.execute("CREATE TABLE orders(order_id INTEGER, customer_id  INTEGER , product_id  INTEGER , quantity INTEGER,order_date INTEGER,price INTEGER)")



# pgcursor.execute("INSERT INTO africa (name,population,gdp,region) VALUES ('Nigeria','200000000',40000,'West')")
# sqlformular = "INSERT INTO africa (name,population, gdp ,region)  VALUES (%s, %s,%s,%s)"
# africa1 = [("Ghana",4500000,1000,"West"), ("Kenya",11000000,2000,"East"), ("South_Africa", 4000000 ,102,"South"),("Mali" ,100000,100,"West")]
# pgcursor.executemany(sqlformular,africa1)


    


# # pgcursor.execute("CREATE TABLE africa(name VARCHAR(255), population INTEGER, gdp INTEGER,region VARCHAR (255))")
# pgcursor.execute("INSERT INTO africa (name,population,gdp,region) VALUES ('Nigeria','200000000',40000,'West')")
# sqlformular = "INSERT INTO africa (name,population, gdp ,region)  VALUES (%s, %s,%s,%s)"
# africa1 = [("Ghana",4500000,1000,"West"), ("Kenya",11000000,2000,"East"), ("South_Africa", 4000000 ,102,"South"),("Mali" ,100000,100,"West")]
# pgcursor.executemany(sqlformular,africa1)

# # pgcursor.execute("UPDATE africa SET name ='Togo' WHERE gdp = 100")
# # pgcursor.execute("UPDATE africa SET gdp =1000 WHERE gdp  < 1000")
# pgcursor.execute("SELECT * FROM africa ORDER BY name")
# # pgcursor.execute("DELETE FROM africa WHERE name = 'Togo'")
# # 
# # mycursor.execute("DROP TABLE Organization")

pgconn.commit()
pgconn.close()


# for x in pgcursor.fetchall():
#       print(x)






# import psycopg2
# import pandas as pd

# # Establish a connection to the database
# pgconn = psycopg2.connect(
#     host="localhost",
#     user="postgres",
#     password="Ayomikun19@",
#     database="mydatabase"
# )

# # Set the isolation level to AUTOCOMMIT
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# pgconn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# # Use Pandas to execute a SQL query and fetch the result into a DataFrame
# # Note: Replace 'mydatabase' with the actual table name you want to query from
# pgpan = pd.read_sql_query('SELECT * FROM africa', con=pgconn)

# # Iterate over the DataFrame columns and print them
# for column in pgpan:
#     print(column)
