import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ayomikun19@',
    database ='testdb'
    )  

print(mydb)  
mycursor = mydb.cursor("") 
mycursor.execute("CREATE DATABASE county")
# mycursor.execute("CREATE TABLE organization(unit VARCHAR(255), no_of_staff INTEGER(10), profit INTEGER(10), best_staff VARCHAR(255))")
# mycursor.execute("INSERT INTO organization (unit,no_of_staff, profit ,best_staff) VALUES ('David','Professor',52,20)")
# sqlformular = "INSERT INTO organization (unit, no_of_staff, profit ,best_staff)  VALUES (%s, %s,%s,%s)"
# organization1 = [("Finance",45,100000,"David"), ("HR",50,100,"Brain"), ("Risk", 40 ,102,"Kano"),("Marketting" ,100,100000,"Ola")]
# mycursor.executemany(sqlformular,organization1)
# mycursor.execute("SELECT name,age FROM lecturers Limit 7 OFFSET 2")
# mycursor.execute("SELECT name,age,person_id FROM staff ")

# mycursor.execute("SELECT * FROM students WHERE age = 20")
# mycursor.execute ("SELECT  * FROM lecturers WHERE position LIKE 'As%'")
# mycursor.execute("SELECT  * FROM students WHERE name LIKE '%e'")
# mycursor.execute("SELECT  * FROM students WHERE name LIKE '%a%'")
# mycursor.execute("UPDATE students SET age = 45 WHERE name = 'Nkechi'")
# # mycursor.execute("UPDATE lecturers SET position = 'Professor' WHERE name = 'Sunday'")
# # mycursor.execute("UPDATE students SET age = 45 WHERE age > 30")
# # mycursor.execute("SELECT * FROM students ORDER BY name")
# mycursor.execute("SELECT * FROM organization ORDER BY profit DESC")
# # mycursor.execute("DELETE FROM students WHERE name = 'Nkechi'")
# mycursor.execute("Delete FROM students WHERE age > 40")
# mycursor.execute("DROP TABLE Organization")




# mycursor.execute("SHOW DATABASES ")
mydb.commit()


# for X in mycursor:
#     print(X)
    
      

