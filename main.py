from tkinter import *
import json
import mysql.connector
from mysql.connector import errorcode

# Функция записи выбранного значения
def remember():
    if len(lbox.curselection()) > 0:
        last_selected = fields[lbox.curselection()[0]]
    if len(last_selected) > 0:
        if last_selected['widget'] == 'spinbox':
            check.update({last_selected['atr']:spin1.get()})
        elif last_selected['widget'] == 'option':
            check.update({last_selected['atr']:option_value})
    print(check)
    weigh()


def get_option(value):
    print(value)
    if value == 'Мужской':
        option_value = 'M'
    elif value == 'Женский':
        option_value = 'F'
    print(option_value)

# Функция выбора элемента из ListBox'a
def select(event):
    if len(lbox.curselection()) > 0:
        last_selected = fields[lbox.curselection()[0]]
        print(str(lbox.curselection()[0])+" - "+last_selected['atr'])
        if last_selected['widget'] == 'option':
            # s1 = StringVar(value=current['values'][0])
            # option1 = OptionMenu(root, s1, current['values'])
            # option1.place(x=190, y=28)
            option1.pack(side=RIGHT)
            spin1.pack_forget()
        elif last_selected['widget'] == 'spinbox':
            # spin1 = Spinbox(root, from_=current['values'][0], to=current['values'][1])
            # spin1.place(x=193,y=88)
            spin1.pack(side=RIGHT)
            option1.pack_forget()

# Функция расчета "весов"
def weigh():
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
        if k > 0:
            w[1] += 1
        w[0] = k if k > w[0] else w[0]
        # weights.update({hd:[k if k > w[0] else w[0], w[1]})
    print(weights)


option_value = ""
last_selected = {}                      # Последний выбранный атрибут
data = []                               # Массив словарей для работы с локальным хранилищем
atr = []  # Список атрибутов
check = {}                              # Список атрибутов, по которым производится сравнение
weights = {'P':[0,0], 'X':[0,0]}        # Список болезнь - "вес" (максимальное число совпавших атрибутов, кол-во таких историй)
# lbox_data = ['Пол', 'Возраст']
fields = [                              # Поля в ListBox'e
    {'field':'Пол', 'atr':'sex', 'widget':'option', 'values':['Мужской','Женский']},
    {'field':'Возраст', 'atr':'age', 'widget':'spinbox', 'values':[0,10]}
]
was_connected = False                   # Удалось соединиться с сервером?
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
# Если поключились, то выгрузить данные из БД в локальное хранилище
if was_connected:
    cursor.execute("select * from directory;")
    atr = [i[0] for i in cursor.description]
    for row in cursor:
        data.append({})
        k = 0
        for col in row:
            if col is not None:
                # if k > len(atr):
                #     data[len(data)-1].update({atr[3]:col})
                # else:
                data[len(data)-1].update({atr[k]:col})
            k += 1
    with open("local_db.json", "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    connection.close()

root = Tk()
root.title('Мед-Анализатор 3000')
root.geometry('500x300')

leb1=Label(root,text='Статические данные')
leb1.place(x=5,y=5)

scrollbar = Scrollbar(root, orient="vertical")

lbox=Listbox(root,width=35,height=15, yscrollcommand=scrollbar.set)
lbox.place(x=5,y=30)
for field in fields:
    lbox.insert(END, field['field'])
lbox.bind('<<ListboxSelect>>', select)

scrollbar.config(command=lbox.yview)
scrollbar.pack(side="right", fill="y")

s1 = StringVar(value='Мужской')
option1 = OptionMenu(root, s1, 'Мужской', 'Женский', command=get_option)
spin1 = Spinbox(root, from_=0, to=10, width=5)

btn = Button(root, text="Запомнить", command=remember)
btn.pack(side=BOTTOM)

root.mainloop()
