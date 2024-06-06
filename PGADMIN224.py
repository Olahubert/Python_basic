import warnings
warnings.filterwarnings('ignore')
import warnings
warnings.filterwarnings('ignore')
import psycopg2
import pandas as pd

pgconn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "Ayomikun19@",
    database = "mydatabase")


# Use the connection object directly with pd.read_sql_query
# pgpan = pd.read_sql(("SELECT * FROM africa WHERE name= 'Nigeria' "), pgconn)

# No need to create a cursor for this operation
# print(pgpan)


my_name= ["John","Jmes","Jude","James" ]
my_name=pd.DataFrame(my_name)
my_name.to_sql("street", pgconn)


