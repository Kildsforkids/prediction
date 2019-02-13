import mysql.connector
from mysql.connector import errorcode

try:
  mariadb_connection = mysql.connector.connect(user='medic', password='medlab',
                                host='deepkom.ru', database='diagmed', port=33547)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("You are connected!")

cursor = mariadb_connection.cursor()

cursor.execute("show tables;")
# cursor.execute("select * from test;")
# cursor.execute("insert into `database`.`test` (`name`) values ('hello');")
# cursor.execute(
#      "CREATE TABLE IF NOT EXISTS `diagmed`.`test` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(100) NOT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;"
# )
#
# mariadb_connection.commit()
for i in cursor:
    print(i)

mariadb_connection.close()
