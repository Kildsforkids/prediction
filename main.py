from tkinter import Tk, Frame, Listbox, Scrollbar, Toplevel, Message, \
    StringVar, IntVar, Spinbox, Button, OptionMenu, Checkbutton
import json
import mysql.connector
from mysql.connector import errorcode
import translations


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


# Функция записи в JSON-файл
def json_write(file, data):
    with open(file, "w") as write_file:
        json.dump(data, write_file)
        write_file.close()


# Функция считывания из JSON-файла
def json_read(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
        read_file.close()
    return data


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
    json_write("local_db.json", data)
    # Удаляем ненужные атрибуты из списка
    atr_list.remove('id')
    atr_list.remove('diagnose')
    json_write("attributes.json", atr_list)


# Функция обновления списка выбранных атрибутов
def outputbox_refresh():
    # Очистить список выбранных атрибутов перед записью
    outputbox.delete(0, outputbox.size()-1)
    for atr in check:
        # Проверка на наличие перевода названия атрибута
        if translations.get(atr) is not None:
            outputbox.insert('end', translations[atr]+' - '+str(check[atr]))
        else:
            outputbox.insert('end', atr+' - '+str(check[atr]))


# Функция записи атрибута в список атрибутов сравнения
def remember():
    widget = ""
    attribute = ""
    # Если есть выбранный ранее атрибут
    if 'last_selected' in globals():
        if len(last_selected) > 0:
            widget = last_selected['widget']
            attribute = last_selected['atr']
            # Запомнить значение атрибута из его виджета
            if widget == 'spinbox':
                str = spin.get()
                if str.isdigit() and len(str) <= 3:
                    check.update({attribute: int(str)})
                    last_selected['values'].clear()
                    last_selected['values'].append(str)
            elif widget == 'option':
                check.update({attribute: option_value.get()})
            elif widget == 'checkbutton':
                check.update({
                    attribute: 'есть' if checkbutton_value.get() else 'нет'
                })
                last_selected['values'].clear()
                last_selected['values'].append(checkbutton_value.get())
            outputbox_refresh()


# Функция удаления атрибута из списка атрибутов сравнения
def forget():
    ocs = outputbox.curselection()
    if len(ocs) > 0:
        id = lbox.get(0, 'end').index(outputbox.get(ocs).split(' -')[0])
        del check[fields[id]['atr']]
        outputbox_refresh()


# Функция удаления всех атрибтов из списка атрибутов сравнения
def forget_all():
    check.clear()
    outputbox_refresh()


# Функция создания виджета для выбранного атрибута
def create_widget():
    if last_selected['widget'] == 'option':
        option.children['menu'].delete(0, 'end')
        for value in last_selected['values']:
            option.children['menu'].add_command(
                label=value,
                command=lambda: option_value.set(value)
            )
        option_value.set(last_selected['values'][0])
        option.place(relx=0.5, rely=0.5, anchor='center')
    elif last_selected['widget'] == 'spinbox':
        if len(last_selected['values']) > 0:
            spin_value.set(last_selected['values'][0])
        else:
            spin_value.set('0')
        spin.place(relx=0.5, rely=0.5, anchor='center')
    elif last_selected['widget'] == 'checkbutton':
        if len(last_selected['values']) > 0:
            checkbutton_value.set(last_selected['values'][0])
        else:
            checkbutton_value.set(0)
        checkbutton.place(relx=0.5, rely=0.5, anchor='center')


# Функция вывода всплывающих сообщений
def show_msg(title, text):
    popup = Toplevel()
    popup.title(title)
    msg = Message(popup, text=text, width=window_width)
    msg.pack()


# Функция выбора атрибута
def select(event):
    global last_selected
    # Если есть текущий выбранный атрибут
    if len(lbox.curselection()) > 0:
        # Записать атрибут как ранее выбранный
        last_selected = fields[lbox.curselection()[0]]
        # Очистить место от предыдущих виджетов
        spin.place_forget()
        option.place_forget()
        checkbutton.place_forget()
        # Установить виджет для соответствующего атрибута
        create_widget()


# Функция анализа
def weigh():
    weight_min_value = 5
    weights = {}
    # Считываем в data данные из JSON-файл
    data = json_read("local_db.json")
    for history in data:
        k = 0
        for attribute in check:
            if history.get(attribute) is not None:
                if check[attribute] == history[attribute]:
                    k += 1
                elif check[attribute] == 'есть':
                    if history[attribute] == 1:
                        k += 1
                elif check[attribute] == 'нет':
                    if history[attribute] == 0:
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
    text = ""
    weights = sorted(weights.items(), key=lambda item: item[1])
    for weight in reversed(weights):
        if weight[1][0] >= weight_min_value and \
           weight[1][1] >= weight_min_value:
            text += '\n'+weight[0]+'\n\tMax: '+str(weight[1][0])+' | People: ' + \
                str(weight[1][1])+'\n'
    if text == "":
        text = "Мало критериев!"
    show_msg("Результат", text)


# Функция создания интерфейса
def main():
    global lbox, outputbox, spin, spin_value, option, option_value, window_width, window_height, \
        checkbutton_value, checkbutton, root

    window_width = 800
    window_height = 600
    listbox_width = window_width // 17

    root = Tk()
    root.title('Мед-Анализатор 3000')
    root.geometry(str(window_width)+'x'+str(window_height))
    root.minsize(window_width, window_height)

    frame = Frame(root)
    frame2 = Frame(root)
    frame.pack(side='left')
    frame2.pack(side='right')

    lbox = Listbox(frame, width=listbox_width, height=window_height)
    lbox.pack(side='left', fill="y")
    for atr in atr_list:
        if translations.get(atr) is not None:
            lbox.insert('end', translations[atr])
        else:
            lbox.insert('end', atr)
    lbox.bind('<<ListboxSelect>>', select)
    lbox.bind('<Double-1>', lambda event: remember())

    outputbox = Listbox(frame2, width=listbox_width, height=window_height)
    outputbox.pack(side='right', fill="y")
    outputbox.bind('<Double-1>', lambda event: forget())

    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=lbox.yview)
    scrollbar.pack(side='right', fill="y")

    scrollbar2 = Scrollbar(frame2, orient="vertical")
    scrollbar2.config(command=outputbox.yview)
    scrollbar2.pack(side='left', fill="y")

    option_value = StringVar(value=fields[0]['values'][0])
    option = OptionMenu(root, option_value, *fields[0]['values'])
    spin_value = StringVar(value='0')
    spin = Spinbox(root, from_=0, to=200, textvariable=spin_value, width=5)
    checkbutton_value = IntVar()
    checkbutton = Checkbutton(text="Есть", variable=checkbutton_value,
                              onvalue=1, offvalue=0)
    root.bind('<Return>', lambda event: remember())
    root.bind('<space>', lambda event: weigh())

    btn = Button(root, text="Запомнить", command=remember)
    btn.pack()

    btn = Button(root, text="Удалить", command=forget)
    btn.pack()

    btn = Button(root, text="Удалить все", command=forget_all)
    btn.pack()

    btn = Button(root, text="Анализировать", command=weigh)
    btn.pack(side='bottom')

    root.mainloop()


if __name__ == '__main__':
    global check, fields, translations, atr_list

    # Словарь для перевода
    translations = translations.get_translation('ru')
    # Список атрибутов и их возможных значений
    fields = []
    # Словарь атрибутов сравнения
    check = {}
    atr_list = []

    connection = connect('62.249.154.246', 'medic', 'medlab', 'diagmed', 33547)
    # Если удалось подключиться
    if connection is not None:
        # Загрузить данные в JSON-файл
        load(connection)
    # Заполнение fields атрибутами и соответстующими им значениями и виджетами
    atr_list = json_read("attributes.json")
    data = json_read("local_db.json")
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

    main()
