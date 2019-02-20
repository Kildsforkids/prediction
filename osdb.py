import mysql.connector
from mysql.connector import errorcode

username = "user"
was_connected = False
cmd = input("Hello, how can I help you? :)\n"+username+": ")
while cmd != "exit":
    if cmd == "help":
        print("\texit - to quit\n\tconnect - to connect to database\n\tinsert\n\tshow")
    elif cmd == "connect":
        try:
            connection = mysql.connector.connect(user='root', password='',
                                        host='localhost', database='diagmed', port=3360)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("You are connected!")
            was_connected = True
            username = "medic"
            cursor = connection.cursor()
    elif cmd == "select":
        cursor.execute("select * from directory;")
        for i in cursor:
            print(i)
    elif cmd == "insert":
        # cursor.execute("insert into `diagmed`.`directory` (`name`) values ('howru');")
        # connection.commit()
    elif cmd == "show":
        cursor.execute("show tables;")
        for i in cursor:
            print(i)
    else:
        print("Unknown command, please, search for help!")
    cmd = input(username+": ")

if was_connected:
    connection.close()
