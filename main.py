from tkinter import *
import json
import mysql.connector
from mysql.connector import errorcode


def select(event):
    print(str(lbox.curselection()[0])+" - "+lbox_data[lbox.curselection()[0]])


def check():
    with open("local_db.json", "r") as read_file:
        data = json.load(read_file)
        read_file.close()
    for history in data:
        k = 0
        for attribute in check:
            if check[attribute] == history[attribute]:
                k += 1
        hd = history['diagnose']
        w = weights[hd]
        weights.update({hd:k if k > w else w})
    print(weights)


data = []
atr = ['id', 'sex', 'age', 'diagnose']
check = {'sex':'M', 'age':51}
weights = {'P':0, 'X':0}
lbox_data = ['Живот','Желчный пузырь(форма)','Размер желчного пузыря(длина)','Размер желчного пузыря(ширина)','Просвет пузыря','Толщина стенок']
was_connected = False
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
    cursor = connection.cursor()
    was_connected = True
if was_connected:
    cursor.execute("select * from directory;")
    for i in cursor:
        data.append({})
        k = 0
        for j in i:
            if j is not None:
                if k > len(atr):
                    data[len(data)-1].update({atr[3]:j})
                else:
                    data[len(data)-1].update({atr[k]:j})
            k += 1
    with open("local_db.json", "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    connection.close()

root = Tk()
root.title('Мед-Анализатор')
root.geometry('500x300')

leb1=Label(root,text='Статические данные')
leb1.place(x=5,y=5)

scrollbar = Scrollbar(root, orient="vertical")

lbox=Listbox(root,width=35,height=15, yscrollcommand=scrollbar.set)
lbox.place(x=5,y=30)
for i in lbox_data:
    lbox.insert(END,i)
lbox.bind('<<ListboxSelect>>', select)

scrollbar.config(command=lbox.yview)
scrollbar.pack(side="right", fill="y")

root.mainloop()
