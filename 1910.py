import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор (Урок 2)")
root.geometry("350x450")

# Переменная для хранения текущего ввода
expression = ""

# --- Пункт 4: Создайте text_input = tk.Label() поле для вывода чисел и знаков при вводе ---
# Изначально пустое, выравнивание текста по правому краю (anchor="e")
text_input = tk.Label(root, text="", font=("Arial", 20), bg="white", anchor="e", padx=10, pady=20)
text_input.pack(fill="x", padx=10, pady=10)

# Поле для вывода результата (из предыдущего задания)
text_result = tk.Label(root, text="", font=("Arial", 16), bg="lightgray", anchor="e", padx=10, pady=10)
text_result.pack(fill="x", padx=10, pady=5)


# --- Пункт 5: Создайте функцию, которая будет назначена на номерные кнопки для ввода значений ---
def button_click(value):
    """
    Эта функция принимает значение (цифру) от кнопки,
    добавляет его к общей строке выражения и обновляет Label.
    """
    global expression
    expression += str(value) # Добавляем символ к строке
    text_input.config(text=expression) # Обновляем текст на экране


# --- Пункт 6: Создайте 5 пустых функций multiply, divide, summy, diff и result ---
# (Они не пустые, а выполняют логику добавления знаков или подсчета)

def multiply():
    global expression
    expression += "*"
    text_input.config(text=expression)

def divide():
    global expression
    expression += "/"
    text_input.config(text=expression)

def summy(): # Сложение
    global expression
    expression += "+"
    text_input.config(text=expression)

def diff(): # Вычитание
    global expression
    expression += "-"
    text_input.config(text=expression)

def result(): # Равно
    global expression
    try:
        # Вычисляем результат
        res = str(eval(expression))
        text_result.config(text=f"= {res}")
    except Exception:
        text_result.config(text="Ошибка")
        expression = "" # Сброс при ошибке


# --- Пункт 2: Создайте интерфейс из 10 кнопок с номерами от 0 до 9 ---
# Создаем фрейм (контейнер) для сетки кнопок
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

# --- Пункт 3 и 4: Матрица и кнопки операций через цикл for ---

# Создадим список кортежей: (Текст кнопки, Строка, Столбец, Функция-обработчик)
# Если функция-обработчик None, значит это цифра (обработаем отдельно в цикле)
buttons_layout = [
    ('7', 0, 0, None), ('8', 0, 1, None), ('9', 0, 2, None), ('/', 0, 3, divide),
    ('4', 1, 0, None), ('5', 1, 1, None), ('6', 1, 2, None), ('*', 1, 3, multiply),
    ('1', 2, 0, None), ('2', 2, 1, None), ('3', 2, 2, None), ('-', 2, 3, diff),
    ('0', 3, 0, None), ('C', 3, 1, None), ('=', 3, 2, result), ('+', 3, 3, summy)
]

for (text, row, col, func) in buttons_layout:
    # Определяем цвет и команду
    if func is not None:
        # Если это операция (/, *, -, +, =)
        command = func
        bg_color = "#cccccc" # Серый
    elif text == 'C':
        # Если это очистка (добавим функционал, хоть в задании и не просили)
        command = lambda: [text_input.config(text=""), text_result.config(text=""), globals().update(expression="")]
        bg_color = "#ff9999" # Красноватый
    else:
        # Если это цифра (0-9)
        # Используем lambda, чтобы передать конкретное значение text в функцию button_click
        # Важно: t=text фиксирует значение переменной на момент создания кнопки
        command = lambda t=text: button_click(t)
        bg_color = "white"

    # Создаем кнопку
    btn = tk.Button(button_frame, text=text, font=("Arial", 14), bg=bg_color, command=command)
    # Размещаем по сетке
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Настраиваем растягивание ячеек
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
