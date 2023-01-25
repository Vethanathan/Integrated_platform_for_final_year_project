# # Host: sql12.freesqldatabase.com
# # Database name: sql12592957
# # Database user: sql12592957
# # Database password: QuJkuAYhUk
# # Port number: 3306
# '''
# meta data :
# CREATE TABLE `sql12592957`.`Details` ( `first_name` VARCHAR(255) NOT NULL , `last_name` VARCHAR(255) NOT NULL , `username` VARCHAR(255) NOT NULL , `password` VARCHAR(255) NOT NULL , PRIMARY KEY (`username`(255))) ENGINE = InnoDB COMMENT = 'This is the table that host the database';



# '''
# import bcrypt
# import mysql.connector

# def hash_it(password):

#     bytes = password.encode('utf-8')
#     hash = bcrypt.hashpw(bytes, b'$2b$12$ikFJLhhV.1ziQsq0cT94IO')
#     return hash




# mydb = mysql.connector.connect(
#     host="sql12.freesqldatabase.com",
#     user="sql12592957",
#     passwd="QuJkuAYhUk",
#     database="sql12592957"
    
# )
# my_cursor = mydb.cursor()
# q="INSERT INTO Details (first_name, last_name, username, password) VALUES ('Vethanathan', 'VK', 'vethanathanvk@gmail.com', 'qwerty@12345');"
# my_cursor.execute(q)
# mydb.commit()
import bcrypt
def hash_it(password):

    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes, b'$2b$12$ikFJLhhV.1ziQsq0cT94IO')
    hash=str(hash)
    return hash[2:-1]

first_name = "Vethanathan"
last_name = "VK"
email = "vethanathanvk@gmail.com"
password="qwerty@12345"

q="INSERT INTO Details (first_name, last_name, username, password) VALUES ('{first_name}', '{last_name}', '{email}', '{password}');".format(first_name=first_name,last_name=last_name,email=email,password=hash_it(password))
print(q)