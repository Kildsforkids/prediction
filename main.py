<<<<<<< HEAD
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
        # Пытаемся установить соединение
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
    # Открываем файл на запись
    with open(file, "w") as write_file:
        # Записываем данные
        json.dump(data, write_file)
        # Закрываем файл
        write_file.close()


# Функция считывания из JSON-файла
def json_read(file):
    # Открываем файл на чтение
    with open(file, "r") as read_file:
        # Считываем данные
        data = json.load(read_file)
        # Закрываем файл
        read_file.close()
    # Возвращаем данные
    return data


# Функция записи данных из БД в JSON-файл
def load(connection):
    # Устанавливаем курсор для SQL-запросов
    cursor = connection.cursor()
    # Получаем результат по отправленному SQL-запросу
    cursor.execute("select * from directory;")
    # Получаем список атрибутов
    atr_list = [i[0] for i in cursor.description]
    # Создаем пустой список для историй болезней
    data = []
    # Перенос записей из БД в data с непустыми атрибутами
    for row in cursor:
        # Добавляем словарь (для записи - атрибут: значение - из БД)
        data.append({})
        # Заводим индекс для перехода к атрибуту с непустым значением
        k = 0
        # Пробегаемся по столбцам и добавляеи записи в словаре -
        # атрибут: значение
        for col in row:
            # Если значение есть
            if col is not None:
                # Обнволяем пары - атрибут: значение -
                # в последнем словаре списка
                data[len(data)-1].update({atr_list[k]: col})
            # Увеличиваем индекс
            k += 1
    # Закрываем подключение к БД
    connection.close()
    # Приводим строковые значения к стандартному виду
    for history in data:
        for key in history:
            # Если не из диагноза и пола
            if key != 'diagnose' and key != 'sex':
                # Если тип значения - строка
                if type(history[key]) is str:
                    # Если строка состоит только из целого числа
                    if history[key].isdigit():
                        # Привести строку к целому числу
                        history[key] = int(history[key])
                    else:
                        # Привести строку к нижнему регистру, без пробелов,
                        # ё = е
                        history[key] = history[key].lower().replace(' ', ''). \
                                                        replace('ё', 'е')
    # Запись из data в JSON-файл
    json_write("local_db.json", data)
    # Удаляем ненужные атрибуты из списка
    atr_list.remove('id')
    atr_list.remove('diagnose')
    # Сохраняем список атрибутов в JSON-файле
    json_write("attributes.json", atr_list)


# Функция заполнения списка словарями - {атрибут, виджет, значения}
def create_fields_list():
    global fields, atr_list

    # Список атрибутов и их возможных значений
    fields = []
    # Получаем список атрибутов
    atr_list = json_read("attributes.json")
    # Получаем данные (истории болезней)
    data = json_read("local_db.json")
    # Для каждого атрибута
    for atr in atr_list:
        # Создаем в списке словарь
        fields.append({})
        # Список значений (если строковые, то для выпадающего меню,
        # если числовые, то для запоминания последнего введенного значения)
        values = []
        # По умолчанию виджет - SpinBox (числовое поле)
        widget_type = 'spinbox'
        # Для каждой истории болезни
        for history in data:
            # Если есть такой атрибут
            if history.get(atr) is not None:
                # Если значение атрибута - строка
                if type(history[atr]) is str:
                    # Если такой строки еще нет
                    if history[atr] not in values:
                        # Добавить строку в список значений
                        # для выпадающего списка (OptionMenu)
                        values.append(history[atr])
                    # Тип виджета - OptionMenu (выпадающий список)
                    widget_type = 'option'
                # Если значение атрибута - целое число
                elif type(history[atr]) is int:
                    # Если атрибут - не возраст
                    if atr != 'age':
                        # Тип виджета - CheckButton (окно с галочкой)
                        widget_type = 'checkbutton'
                    break
                # Если значение атрибута - вещественное число
                elif type(history[atr]) is float:
                    # Тип виджета - SpinBox
                    # (числовое поле для вещественных чисел)
                    widget_type = 'spinbox_float'
                    break
                else:
                    break
        # Записать словарь
        # {'atr': название атрибута,
        #  'widget': тип виджета,
        #  'values': значения атрибута
        # } в список словарей
        fields[len(fields)-1].update({'atr': atr})
        fields[len(fields)-1].update({'widget': widget_type})
        fields[len(fields)-1].update({'values': values})


# Проверка на минимальное количество выбранных атрибутов для доступа к анализу
def check_outputbox():
    # Если атрибутов >= чем минимальное
    if outputbox.size() >= weight_min_value:
        # Сделать активной кнопку "Анализировать"
        weigh_btn['state'] = 'normal'
    else:
        # Сделать неактивной кнопку ""Анализировать
        weigh_btn['state'] = 'disabled'


# Функция обновления списка выбранных атрибутов
def outputbox_refresh():
    # Очистить список выбранных атрибутов перед записью
    outputbox.delete(0, outputbox.size()-1)
    for atr in check:
        # Проверка на наличие перевода названия атрибута
        if translations.get(atr) is not None:
            # Перевести название атрибута и добавить
            # в список выбранных атрибтов для сравнения
            outputbox.insert('end', translations[atr]+' - '+str(check[atr]))
        else:
            # Добавить атрибут без перевода
            outputbox.insert('end', atr+' - '+str(check[atr]))
    # Проверить на минимальное количество выбранных атрибутов
    check_outputbox()


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
                string = spin.get()
                if string.isdigit() and len(string) <= 3:
                    check.update({attribute: int(string)})
                    last_selected['values'].clear()
                    last_selected['values'].append(string)
            elif widget == 'option':
                check.update({attribute: option_value.get()})
            elif widget == 'checkbutton':
                check.update({
                    attribute: 'есть' if checkbutton_value.get() else 'нет'
                })
                last_selected['values'].clear()
                last_selected['values'].append(checkbutton_value.get())
            elif widget == 'spinbox_float':
                string = spin.get()
                can = True
                try:
                    float(string)
                except ValueError:
                    can = False
                if can:
                    check.update({attribute: float(string)})
                    last_selected['values'].clear()
                    last_selected['values'].append(string)
            # Обновить список выбранных атрибутов
            outputbox_refresh()


# Функция удаления атрибута из списка атрибутов сравнения
def forget():
    # Получаем текущий выбранный элемент
    ocs = outputbox.curselection()
    # Если есть выбранный элемент
    if len(ocs) > 0:
        # Получаем индекс
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
    elif last_selected['widget'] == 'spinbox' or \
            last_selected['widget'] == 'spinbox_float':
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
    # weight_min_value = 5
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
        checkbutton_value, checkbutton, root, weigh_btn

    window_width = 800
    window_height = 600
    listbox_width = window_width // 17

    root = Tk()
    root.title('Мед-Анализатор 3000')
    root.geometry(str(window_width)+'x'+str(window_height))
    root.minsize(window_width, window_height)
    root.maxsize(window_width, window_height)
    root.bind('<Return>', lambda event: remember())

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
    spin = Spinbox(root, from_=0, to=200, textvariable=spin_value, width=5,
                   format="%.2f")
    checkbutton_value = IntVar()
    checkbutton = Checkbutton(text="Есть", variable=checkbutton_value,
                              onvalue=1, offvalue=0)

    btn = Button(root, text="Запомнить", command=remember)
    btn.pack()

    btn = Button(root, text="Удалить", command=forget)
    btn.pack()

    btn = Button(root, text="Удалить все", command=forget_all)
    btn.pack()

    weigh_btn = Button(root, text="Анализировать", state='disabled',
                       padx=5, pady=5, command=weigh)
    weigh_btn.pack(side='bottom')

    root.mainloop()


if __name__ == '__main__':
    global check, fields, translations, atr_list, weight_min_value

    # Словарь для перевода
    translations = translations.get_translation('ru')
    # Словарь атрибутов сравнения
    check = {}
    # Минимальное необходимое число для критериев Max и People
    weight_min_value = 5
    # Попытка подключения к БД
    connection = connect('62.249.154.246', 'medic', 'medlab', 'diagmed', 33547)
    # Если удалось подключиться
    if connection is not None:
        # Загрузить данные в JSON-файл
        load(connection)
    # Заполнение fields атрибутами и соответстующими им значениями и виджетами
    create_fields_list()
    # Запуск интерфейса
    main()
=======
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
        # Пытаемся установить соединение
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
    # Открываем файл на запись
    with open(file, "w") as write_file:
        # Записываем данные
        json.dump(data, write_file)
        # Закрываем файл
        write_file.close()


# Функция считывания из JSON-файла
def json_read(file):
    # Открываем файл на чтение
    with open(file, "r") as read_file:
        # Считываем данные
        data = json.load(read_file)
        # Закрываем файл
        read_file.close()
    # Возвращаем данные
    return data


# Функция записи данных из БД в JSON-файл
def load(connection):
    # Устанавливаем курсор для SQL-запросов
    cursor = connection.cursor()
    # Получаем результат по отправленному SQL-запросу
    cursor.execute("select * from directory;")
    # Получаем список атрибутов
    atr_list = [i[0] for i in cursor.description]
    # Создаем пустой список для историй болезней
    data = []
    # Перенос записей из БД в data с непустыми атрибутами
    for row in cursor:
        # Добавляем словарь (для записи - атрибут: значение - из БД)
        data.append({})
        # Заводим индекс для перехода к атрибуту с непустым значением
        k = 0
        # Пробегаемся по столбцам и добавляеи записи в словаре -
        # атрибут: значение
        for col in row:
            # Если значение есть
            if col is not None:
                # Обнволяем пары - атрибут: значение -
                # в последнем словаре списка
                data[len(data)-1].update({atr_list[k]: col})
            # Увеличиваем индекс
            k += 1
    # Закрываем подключение к БД
    connection.close()
    # Приводим строковые значения к стандартному виду
    for history in data:
        for key in history:
            # Если не из диагноза и пола
            if key != 'diagnose' and key != 'sex':
                # Если тип значения - строка
                if type(history[key]) is str:
                    # Если строка состоит только из целого числа
                    if history[key].isdigit():
                        # Привести строку к целому числу
                        history[key] = int(history[key])
                    else:
                        # Привести строку к нижнему регистру, без пробелов,
                        # ё = е
                        history[key] = history[key].lower().replace(' ', ''). \
                                                        replace('ё', 'е')
    # Запись из data в JSON-файл
    json_write("local_db.json", data)
    # Удаляем ненужные атрибуты из списка
    atr_list.remove('id')
    atr_list.remove('diagnose')
    # Сохраняем список атрибутов в JSON-файле
    json_write("attributes.json", atr_list)


# Функция заполнения списка словарями - {атрибут, виджет, значения}
def create_fields_list():
    global fields, atr_list

    # Список атрибутов и их возможных значений
    fields = []
    # Получаем список атрибутов
    atr_list = json_read("attributes.json")
    # Получаем данные (истории болезней)
    data = json_read("local_db.json")
    # Для каждого атрибута
    for atr in atr_list:
        # Создаем в списке словарь
        fields.append({})
        # Список значений (если строковые, то для выпадающего меню,
        # если числовые, то для запоминания последнего введенного значения)
        values = []
        # По умолчанию виджет - SpinBox (числовое поле)
        widget_type = 'spinbox'
        # Для каждой истории болезни
        for history in data:
            # Если есть такой атрибут
            if history.get(atr) is not None:
                # Если значение атрибута - строка
                if type(history[atr]) is str:
                    # Если такой строки еще нет
                    if history[atr] not in values:
                        # Добавить строку в список значений
                        # для выпадающего списка (OptionMenu)
                        values.append(history[atr])
                    # Тип виджета - OptionMenu (выпадающий список)
                    widget_type = 'option'
                # Если значение атрибута - целое число
                elif type(history[atr]) is int:
                    # Если атрибут - не возраст
                    if atr != 'age':
                        # Тип виджета - CheckButton (окно с галочкой)
                        widget_type = 'checkbutton'
                    break
                # Если значение атрибута - вещественное число
                elif type(history[atr]) is float:
                    # Тип виджета - SpinBox
                    # (числовое поле для вещественных чисел)
                    widget_type = 'spinbox_float'
                    break
                else:
                    break
        # Записать словарь
        # {'atr': название атрибута,
        #  'widget': тип виджета,
        #  'values': значения атрибута
        # } в список словарей
        fields[len(fields)-1].update({'atr': atr})
        fields[len(fields)-1].update({'widget': widget_type})
        fields[len(fields)-1].update({'values': values})


# Проверка на минимальное количество выбранных атрибутов для доступа к анализу
def check_outputbox():
    # Если атрибутов >= чем минимальное
    if outputbox.size() >= weight_min_value:
        # Сделать активной кнопку "Анализировать"
        weigh_btn['state'] = 'normal'
    else:
        # Сделать неактивной кнопку ""Анализировать
        weigh_btn['state'] = 'disabled'


# Функция обновления списка выбранных атрибутов
def outputbox_refresh():
    # Очистить список выбранных атрибутов перед записью
    outputbox.delete(0, outputbox.size()-1)
    for atr in check:
        # Проверка на наличие перевода названия атрибута
        if translations.get(atr) is not None:
            # Перевести название атрибута и добавить
            # в список выбранных атрибтов для сравнения
            outputbox.insert('end', translations[atr]+' - '+str(check[atr]))
        else:
            # Добавить атрибут без перевода
            outputbox.insert('end', atr+' - '+str(check[atr]))
    # Проверить на минимальное количество выбранных атрибутов
    check_outputbox()


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
                string = spin.get()
                if string.isdigit() and len(string) <= 3:
                    check.update({attribute: int(string)})
                    last_selected['values'].clear()
                    last_selected['values'].append(string)
            elif widget == 'option':
                check.update({attribute: option_value.get()})
            elif widget == 'checkbutton':
                check.update({
                    attribute: 'есть' if checkbutton_value.get() else 'нет'
                })
                last_selected['values'].clear()
                last_selected['values'].append(checkbutton_value.get())
            elif widget == 'spinbox_float':
                string = spin.get()
                can = True
                try:
                    float(string)
                except ValueError:
                    can = False
                if can:
                    check.update({attribute: float(string)})
                    last_selected['values'].clear()
                    last_selected['values'].append(string)
            # Обновить список выбранных атрибутов
            outputbox_refresh()


# Функция удаления атрибута из списка атрибутов сравнения
def forget():
    # Получаем текущий выбранный элемент
    ocs = outputbox.curselection()
    # Если есть выбранный элемент
    if len(ocs) > 0:
        # Получаем индекс
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
    elif last_selected['widget'] == 'spinbox' or \
            last_selected['widget'] == 'spinbox_float':
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
    # weight_min_value = 5
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
        checkbutton_value, checkbutton, root, weigh_btn

    window_width = 800
    window_height = 600
    listbox_width = window_width // 17

    root = Tk()
    root.title('Мед-Анализатор 3000')
    root.geometry(str(window_width)+'x'+str(window_height))
    root.minsize(window_width, window_height)
    root.maxsize(window_width, window_height)
    root.bind('<Return>', lambda event: remember())

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
    spin = Spinbox(root, from_=0, to=200, textvariable=spin_value, width=5,
                   format="%.2f")
    checkbutton_value = IntVar()
    checkbutton = Checkbutton(text="Есть", variable=checkbutton_value,
                              onvalue=1, offvalue=0)

    btn = Button(root, text="Запомнить", command=remember)
    btn.pack()

    btn = Button(root, text="Удалить", command=forget)
    btn.pack()

    btn = Button(root, text="Удалить все", command=forget_all)
    btn.pack()

    weigh_btn = Button(root, text="Анализировать", state='disabled',
                       padx=5, pady=5, command=weigh)
    weigh_btn.pack(side='bottom')

    root.mainloop()


if __name__ == '__main__':
    global check, fields, translations, atr_list, weight_min_value

    # Словарь для перевода
    translations = translations.get_translation('ru')
    # Словарь атрибутов сравнения
    check = {}
    # Минимальное необходимое число для критериев Max и People
    weight_min_value = 5
    # Попытка подключения к БД
    connection = connect('62.249.154.246', 'medic', 'medlab', 'diagmed', 33547)
    # Если удалось подключиться
    if connection is not None:
        # Загрузить данные в JSON-файл
        load(connection)
    # Заполнение fields атрибутами и соответстующими им значениями и виджетами
    create_fields_list()
    # Запуск интерфейса
    main()
>>>>>>> 6df53266bb27b333f69d90477c9a2cc2b82fd23d
