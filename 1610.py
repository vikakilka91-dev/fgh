import tkinter as tk

# --- Пункт 1: Установка библиотеки (выполняется в терминале: pip install tkinter, но для встроенного модуля это не обязательно) ---

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("350x450") # Задаем размер окна

# Переменная для хранения введенного текста (чтобы удобно считывать)
expression = ""

# --- Пункт 4: Создайте text_input = tk.Label() поле для вывода чисел и знаков при вводе (нажатии) ---
# Используем Label вместо Entry, так как в задании указан именно Label, но для красоты можно использовать Entry с состоянием 'readonly'
text_input = tk.Label(root, text="", font=("Arial", 20), bg="white", anchor="e", padx=10, pady=20)
text_input.pack(fill="x", padx=10, pady=10)

# --- Пункт 5: Создайте text result = tk.Label() поле для вывода результата операции ---
text_result = tk.Label(root, text="", font=("Arial", 16), bg="lightgray", anchor="e", padx=10, pady=10)
text_result.pack(fill="x", padx=10, pady=5)

# Функция для обновления верхнего поля
def update_input(value):
    global expression
    expression += str(value)
    text_input.config(text=expression)

# Функции для операций (Пункт 6)
def multiply():
    global expression
    try:
        # Вычисляем текущее значение и добавляем знак умножения
        # В Python знак умножения это *
        update_input("*")
    except:
        pass

def divide():
    global expression
    try:
        update_input("/")
    except:
        pass

def summy(): # Сложение
    global expression
    update_input("+")

def diff(): # Вычитание
    global expression
    update_input("-")

def result(): # Равно
    global expression
    try:
        # Выполняем математическое выражение
        # eval - опасная функция, но для простого калькулятора допустима
        res = str(eval(expression))
        text_result.config(text=f"Результат: {res}")
        # Можно сбросить expression, если нужно начать заново, или оставить для продолжения
        # expression = res 
    except Exception:
        text_result.config(text="Ошибка")
        expression = ""

# --- Пункт 2: Создайте интерфейс из 10 кнопок с номерами от 0 до 9 (tk.Button) ---
# --- Пункт 3: Создайте матрицу с названиями функций и знаками операций ---

# Создаем фрейм для сетки кнопок
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Список кнопок для цифр и операций
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

# --- Пункт 4 (продолжение): через цикл for задайте text и command ---
# Проходимся по списку и создаем кнопки
for (text, row, col) in buttons:
    # Определяем действие для кнопки
    if text.isdigit():
        # Если это цифра
        cmd = lambda t=text: update_input(t)
        bg_color = "white"
    elif text == 'C':
        # Очистка
        cmd = lambda: [text_input.config(text=""), text_result.config(text=""), globals().update(expression="")]
        bg_color = "#ff9999"
    elif text == '=':
        # Результат
        cmd = result
        bg_color = "#99ff99"
    elif text == '+':
        cmd = summy
        bg_color = "#cccccc"
    elif text == '-':
        cmd = diff
        bg_color = "#cccccc"
    elif text == '*':
        cmd = multiply
        bg_color = "#cccccc"
    elif text == '/':
        cmd = divide
        bg_color = "#cccccc"
    else:
        cmd = None
        bg_color = "#cccccc"

    # Создаем кнопку
    btn = tk.Button(button_frame, text=text, font=("Arial", 14), bg=bg_color, command=cmd)
    # Размещаем в сетке
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Настраиваем веса строк и столбцов для растягивания
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Запуск приложения
root.mainloop()
