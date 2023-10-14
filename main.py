# Импорт нужного
import sqlite3
import tkinter as tk
import webbrowser


# Создание таблиц с работниками
def create_table():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 phone TEXT,
                 email TEXT,
                 salary REAL)''')
    conn.commit()
    conn.close()


# Вставка работников в таблицу
def insert_employee():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    salary = entry_salary.get()

    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)",
              (name, phone, email, salary))
    conn.commit()
    conn.close()
    # Показ в Приложении
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


# Поиск по сотрудникам
def search_employee():
    name = entry_search.get()

    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    rows = c.fetchall()
    conn.close()

    result_text.delete(1.0, tk.END)
    for row in rows:
        result_text.insert(tk.END, row[1] + ": " + row[2] + ", " + row[3] + ", " + str(row[4]) + "\n")


# Удаляем сотрудников
def delete_employee():
    name = entry_search.get()

    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    conn.commit()
    conn.close()

    entry_search.delete(0, tk.END)
    result_text.delete(1.0, tk.END)


# Измненение/Обновление работника
def update_employee():
    name = entry_search.get()
    new_name = entry_name.get()
    new_phone = entry_phone.get()
    new_email = entry_email.get()
    new_salary = entry_salary.get()

    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("UPDATE employees SET name=?, phone=?, email=?, salary=? WHERE name LIKE ?",
              (new_name, new_phone, new_email, new_salary, '%' + name + '%'))
    conn.commit()
    conn.close()

    entry_search.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


def link():
    pass


# ДАЛЬШЕ ИДЁТ TKINTER!


# Создание приложения в Tkinter
root = tk.Tk()
root.title("Список сотрудников компании")
root.geometry("512x512")
# пак с Именем фамилией и отчество
label_name = tk.Label(root, text="ФИО")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()
# Столбец с номером телефона
label_phone = tk.Label(root, text="Номер телефона")
label_phone.pack()
entry_phone = tk.Entry(root)
entry_phone.pack()
# Столбец с эл. Почтой
label_email = tk.Label(root, text="Адрес электронной почты")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()
# Столбец с зарплатой
label_salary = tk.Label(root, text="Заработная плата")
label_salary.pack()
entry_salary = tk.Entry(root)
entry_salary.pack()


# Полноэкранный режим
def fullscreen(e=None):
    if root.attributes('-fullscreen'):  # Проверяем режим окна
        root.attributes('-fullscreen', False)  # Меняем режим окна
    else:
        root.attributes('-fullscreen', True)  # Меняем режим окна


root.bind('<F11>', fullscreen)  # Биндим окно

# def on_close(e=None):
#    pass  # Мы просто ничего не делаем
# Можно так же спрашивать пользователя ВЫ ТОЧНО ХОТИТЕ ЗАКРЫТЬ ОКНО ?
# root.protocol("WM_DELETE_WINDOW", on_close) Перехватываем событие выхода из приложения
# И человек никогда больше не закрывает наше приложение=)

# КНОПКИ! КРАСИВЫЙ КНОПКА!


# Кнопка добавить сотрудника
button_insert = tk.Button(root, text="Добавить рабочего", command=insert_employee)


def focus_in(e=None):
    button_insert.configure(fg='#fff')
    button_insert.configure(bg='#000')


def focus_out(e=None):
    button_insert.configure(bg='#fff')
    button_insert.configure(fg='#000')


button_insert.bind('<Enter>', focus_in)  # При входе курсора в область кнопки выполняем focus_in
button_insert.bind('<Leave>', focus_out)  # При выходе курсора из области кнопки выполняем focus_out_out
button_insert.pack()

# Кнопка поиска
label_search = tk.Label(root, text="Поиск по ФИО")
label_search.pack()
entry_search = tk.Entry(root)
entry_search.pack()
# Кнопка поиска сотрудника
button_search = tk.Button(root, text="Найти рабочего", command=search_employee)


def focus_in(e=None):
    button_search.configure(fg='#fff')
    button_search.configure(bg='#000')


def focus_out(e=None):
    button_search.configure(bg='#fff')
    button_search.configure(fg='#000')


button_search.bind('<Enter>', focus_in)  # При входе курсора в область кнопки выполняем focus_in
button_search.bind('<Leave>', focus_out)  # При выходе курсора из области кнопки выполняем focus_out_out
button_search.pack()

# Показ результата из приложения
result_text = tk.Text(root, height=10, width=50)
result_text.pack()
# Удаляет сотрудника
button_delete = tk.Button(root, text="Удалить рабочего", command=delete_employee)


def focus_in(e=None):
    button_delete.configure(fg='#fff')
    button_delete.configure(bg='#000')


def focus_out(e=None):
    button_delete.configure(bg='#fff')
    button_delete.configure(fg='#000')


button_delete.bind('<Enter>', focus_in)  # При входе курсора в область кнопки выполняем focus_in
button_delete.bind('<Leave>', focus_out)  # При выходе курсора из области кнопки выполняем focus_out_out
button_delete.pack()

# Изменяет сотрудника
button_update = tk.Button(root, text="Изменить рабочего", command=update_employee)


def focus_in(e=None):
    button_update.configure(fg='#fff')
    button_update.configure(bg='#000')


def focus_out(e=None):
    button_update.configure(bg='#fff')
    button_update.configure(fg='#000')


button_update.bind('<Enter>', focus_in)  # При входе курсора в область кнопки выполняем focus_in
button_update.bind('<Leave>', focus_out)  # При выходе курсора из области кнопки выполняем focus_out_out
button_update.pack()


def link(e=None):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')  # Открываем браузер

button = tk.Button(root, command=link, padx=3, pady=3,
                    text='Бонус от разработчика!', bd=0, fg='#fff',
                    bg='#08f', underline=0,
                   activebackground='#fff',
                   activeforeground='#fff', cursor='hand2')  # Инициализация кнопки
button.pack(expand=2)  # Размещение кнопки по центру окна

create_table()
root.mainloop()
