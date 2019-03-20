from tkinter import Tk, Frame, Listbox, Scrollbar, Toplevel, Message, \
    END, CENTER, LEFT, RIGHT, BOTTOM, StringVar, IntVar, Spinbox, Button, \
    OptionMenu, Checkbutton
import json
import mysql.connector
from mysql.connector import errorcode
import translations
# import time


# Функция соединения с БД
def connect(host, user, password, database, port):
    connection = None
    try:
        connection = mysql.connector.connect(user=user, password=password,
                                             host=host, database=database,
                                             port=port)
    except mysql.connector.Error as err:
        # Если неверны данные для подключения
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        # Если БД не существует
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        # Другие виды ошибок
        else:
            print(err)
    # При успешном подключении
    else:
        print("You are connected!")
    # Возвращает None
    return connection


# Функция записи данных из БД в JSON-файл
def load(connection):
    cursor = connection.cursor()
    # Получаем результат по отправленному SQL-запросу
    cursor.execute("select * from directory;")
    # Получаем список атрибутов
    atr_list = [i[0] for i in cursor.description]
    data = []
    # Перенос записей из БД в data с непустыми атрибутами
    for row in cursor:
        data.append({})
        k = 0
        for col in row:
            if col is not None:
                data[len(data)-1].update({atr_list[k]: col})
            k += 1
    connection.close()
    # Запись из data в JSON-файл
    with open("local_db.json", "w") as write_file:
        json.dump(data, write_file)
        write_file.close()
    # Удаляем ненужные атрибуты из списка
    atr_list.remove('id')
    atr_list.remove('diagnose')
    with open("attributes.json", "w") as write_file:
        json.dump(atr_list, write_file)
        write_file.close()


# Функция обновления списка выбранных атрибутов
def outputbox_refresh():
    # Очистить список выбранных атрибутов перед записью
    outputbox.delete(0, outputbox.size()-1)
    for atr in check:
        # Проверка на наличие перевода названия атрибута
        if translations.get(atr) is not None:
            outputbox.insert(END, translations[atr]+' - '+str(check[atr]))
        else:
            outputbox.insert(END, atr+' - '+str(check[atr]))


# Функция записи атрибута в список атрибутов сравнения
def remember(event):
    widget = ""
    attribute = ""
    # Если есть выбранный ранее атрибут
    if len(last_selected) > 0:
        widget = last_selected['widget']
        attribute = last_selected['atr']
        # Запомнить значение атрибута из его виджета
        if widget == 'spinbox':
            if spin1.get() != '':
                check.update({attribute: int(spin1.get())})
        elif widget == 'option':
            check.update({attribute: s1.get()})
        elif widget == 'checkbutton':
            check.update({attribute: cbv.get()})
        outputbox_refresh()
    # print(check)


# Функция удаления атрибута из списка атрибутов сравнения
def forget(event):
    ocs = outputbox.curselection()
    if len(ocs) > 0:
        id = lbox.get(0, END).index(outputbox.get(ocs).split(' -')[0])
        del check[fields[id]['atr']]
        outputbox_refresh()
        # print(check)


# Функция выбора атрибута
def select(event):
    global last_selected
    # Если есть текущий выбранный атрибут
    if len(lbox.curselection()) > 0:
        # Записать атрибут как ранее выбранный
        last_selected = fields[lbox.curselection()[0]]
        # Очистить место от предыдущих виджетов
        spin1.place_forget()
        option1.place_forget()
        checkbutton.place_forget()
        # Установить виджет для соответствующего атрибута
        if last_selected['widget'] == 'option':
            option1.children['menu'].delete(0, END)
            for value in last_selected['values']:
                option1.children['menu'].add_command(
                    label=value,
                    command=lambda: s1.set(value)
                )
            s1.set(last_selected['values'][0])
            option1.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif last_selected['widget'] == 'spinbox':
            spin1.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif last_selected['widget'] == 'checkbutton':
            checkbutton.place(relx=0.5, rely=0.5, anchor=CENTER)


def outputbox_select(event):
    ocs = outputbox.curselection()
    if len(ocs) > 0:
        id = lbox.get(0, END).index(outputbox.get(ocs).split(' -')[0])
        print(fields[id]['atr'])


# Функция анализа
def weigh():
    weights = {}
    # Считываем в data данные из JSON-файл
    with open("local_db.json", "r") as read_file:
        data = json.load(read_file)
        read_file.close()
    # Поиск подходящих совпадений
    for history in data:
        k = 0
        for attribute in check:
            if history.get(attribute) is not None:
                print(check[attribute], history[attribute])
                if check[attribute] == history[attribute]:
                    k += 1
        hd = history['diagnose']
        if hd not in weights:
            weights.update({hd: [0, 0]})
        w = weights[hd]
        if k > 0:
            w[1] += 1
        w[0] = k if k > w[0] else w[0]
        weights.update({hd: [w[0], w[1]]})
    # Вывод результатов в отдельном окне
    popup = Toplevel()
    popup.title("Результат")
    text = ""
    for weight in weights:
        if weights[weight][0] or weights[weight][1]:
            if weights[weight][0] >= 3:
                text += weight+' '+str(weights[weight][0])+' ' + \
                    str(weights[weight][1])+'\n'
                print(weight, weights[weight][0], weights[weight][1])
    msg = Message(popup, text=text, width=window_width)
    msg.pack()


# Функция создания интерфейса
def main():
    global lbox, outputbox, spin1, option1, s1, window_width, window_height, \
        cbv, checkbutton, root

    window_width = 640
    window_height = 480

    root = Tk()
    root.title('Мед-Анализатор 3000')
    root.geometry(str(window_width)+'x'+str(window_height))

    frame = Frame(root)
    frame2 = Frame(root)
    frame.pack(side=LEFT)
    frame2.pack(side=RIGHT)

    lbox = Listbox(frame, width=40, height=window_height)
    lbox.pack(side=LEFT, fill="y")
    for atr in atr_list:
        if translations.get(atr) is not None:
            lbox.insert(END, translations[atr])
        else:
            lbox.insert(END, atr)
    lbox.bind('<<ListboxSelect>>', select)
    lbox.bind('<Double-1>', remember)

    outputbox = Listbox(frame2, width=40, height=window_height)
    outputbox.pack(side=RIGHT, fill="y")
    outputbox.bind('<Double-1>', forget)

    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=lbox.yview)
    scrollbar.pack(side=RIGHT, fill="y")

    scrollbar2 = Scrollbar(frame2, orient="vertical")
    scrollbar2.config(command=outputbox.yview)
    scrollbar2.pack(side=LEFT, fill="y")

    s1 = StringVar(value=fields[0]['values'][0])
    option1 = OptionMenu(root, s1, *fields[0]['values'])
    spin1 = Spinbox(root, width=5)

    btn = Button(root, text="Запомнить", command=remember)
    btn.pack()

    btn = Button(root, text="Удалить", command=forget)
    btn.pack()

    btn = Button(root, text="Анализировать", command=weigh)
    btn.pack(side=BOTTOM)

    cbv = IntVar()
    checkbutton = Checkbutton(text="Есть", variable=cbv, onvalue=1,
                              offvalue=0)

    root.mainloop()


if __name__ == '__main__':
    global check, fields, translations, atr_list

    # Словарь для перевода
    translations = translations.get_translation('ru')
    # Список атрибутов и их возможных значений
    fields = []
    # fields = [
    #     {'atr': 'sex', 'widget': 'option',
    #      'values': ['М', 'Ж']},
    #     {'atr': 'age', 'widget': 'spinbox',
    #      'values': [0, 200]},
    #     {'atr': 'tongue', 'widget': 'option',
    #      'values': ['нет', 'белый', 'желтый', 'серый']},
    #     {'atr': 'stomach', 'widget': 'option',
    #      'values': ['мягкий', 'твердый']},
    #     {'atr': 'gallbladder_bending',
    #      'widget': 'checkbutton', 'values': 'Есть'}
    # ]
    # Словарь атрибутов сравнения
    check = {}
    atr_list = []

    connection = connect('62.249.154.246', 'medic', 'medlab', 'diagmed', 33547)
    # Если удалось подключиться
    if connection is not None:
        # Загрузить данные в JSON-файл
        load(connection)
    # Заполнение fields атрибутами и соответстующими им значениями и виджетами
    with open("attributes.json", "r") as read_file:
        atr_list = json.load(read_file)
        read_file.close()
    with open("local_db.json", "r") as read_file:
        data = json.load(read_file)
        for atr in atr_list:
            fields.append({})
            values = []
            widget_type = 'spinbox'
            for history in data:
                if history.get(atr) is not None:
                    if type(history[atr]) is str:
                        if history[atr] not in values:
                            values.append(history[atr])
                    elif type(history[atr]) is int:
                        if atr != 'age':
                            widget_type = 'checkbutton'
                        break
                    elif type(history[atr]) is float:
                        # print(atr, history[atr])
                        break
                    else:
                        break
            if len(values) > 0:
                widget_type = 'option'
            fields[len(fields)-1].update({'atr': atr})
            fields[len(fields)-1].update({'widget': widget_type})
            fields[len(fields)-1].update({'values': values})
        read_file.close()

    main()
