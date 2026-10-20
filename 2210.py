import tkinter as tk
import math

# Глобальная переменная для хранения введенного математического выражения
expression = ""

def update_display():
    """Вспомогательная функция для обновления текста на экране"""
    text_input.config(text=expression)

# --- Пункт 5 и 6: Функция обработки нажатий (цифры и операторы) и вычисления ---
def on_button_click(char):
    global expression
    
    # --- Пункт 7: Единичные конструкции if-else ---
    if char == "=":
        # Пункт 6: В функции сохраняйте результат ввода и вывода, обрабатывайте общее значение при нажатии на "="
        try:
            # Проверка на пустую строку
            if expression == "":
                return
                
            # Заменяем символы для Python (например, если бы использовали x вместо *, но здесь все прямо)
            # Функция eval вычисляет строку как математическое выражение
            result = eval(expression)
            
            # Проверка результата на бесконечность (например, при делении на ноль)
            if isinstance(result, float) and (math.isinf(result) or math.isnan(result)):
                text_result.config(text="Ошибка: Деление на 0")
                expression = ""
            else:
                text_result.config(text="= " + str(result))
                expression = str(result) # Сохраняем результат для дальнейших вычислений
                update_display()
                
        except ZeroDivisionError:
            text_result.config(text="Ошибка: Деление на 0")
            expression = ""
        except Exception:
            text_result.config(text="Ошибка ввода")
            expression = ""
            
    elif char == "C":
        # Очистка
        expression = ""
        text_result.config(text="")
        update_display()
        
    else:
        # Ввод цифр и операторов
        expression += str(char)
        update_display()


# --- Инициализация окна ---
root = tk.Tk()
root.title("Калькулятор (Урок 9)")
root.geometry("350x450")
root.configure(bg="#2d2d2d")

# --- Пункт 4: Создайте text_input = tk.Label() поле для вывода чисел и знаков ---
text_input = tk.Label(root, text="", font=("Arial", 24), bg="#ffffff", anchor="e", padx=10, pady=20)
text_input.pack(fill="x", padx=10, pady=(20, 5))

# Поле для вывода результата (из предыдущего задания)
text_result = tk.Label(root, text="", font=("Arial", 16), bg="#e0e0e0", anchor="e", padx=10, pady=10)
text_result.pack(fill="x", padx=10, pady=5)

# Фрейм для кнопок
button_frame = tk.Frame(root, bg="#2d2d2d")
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

# --- Пункт 3: Создайте массив с знаками арифметических операций ---
operators = ["+", "-", "*", "/"]

# --- Пункт 2 и 4: Интерфейс и кнопки операций через цикл for ---
# Создаем единый массив всех кнопок для цикла for (Пункт 7 - используем только цикл for)
# Формат: (Текст, Строка, Столбец, Категория)
# Категории: 'num' (цифра), 'op' (оператор), 'act' (действие)
buttons_data = [
    ('7', 0, 0, 'num'), ('8', 0, 1, 'num'), ('9', 0, 2, 'num'), ('/', 0, 3, 'op'),
    ('4', 1, 0, 'num'), ('5', 1, 1, 'num'), ('6', 1, 2, 'num'), ('*', 1, 3, 'op'),
    ('1', 2, 0, 'num'), ('2', 2, 1, 'num'), ('3', 2, 2, 'num'), ('-', 2, 3, 'op'),
    ('0', 3, 0, 'num'), ('C', 3, 1, 'act'), ('=', 3, 2, 'act'), ('+', 3, 3, 'op')
]

# --- Пункт 7: Только цикл for для создания интерфейса ---
for (text, row, col, category) in buttons_data:
    
    # Настройка цвета в зависимости от типа кнопки
    if category == 'num':
        bg_color = "#4d4d4d"
        fg_color = "white"
    elif category == 'op':
        bg_color = "#ff9500" # Оранжевый как в iOS
        fg_color = "white"
    elif text == '=':
        bg_color = "#34c759" # Зеленый
        fg_color = "white"
    else:
        bg_color = "#a5a5a5" # Серый
        fg_color = "black"

    # --- Пункт 4: Через цикл for задайте text и command ---
    # Для цифр и операций используем лямбда-функцию с фиксацией значения (t=text)
    # Для очистки и равно тоже передаем символ
    btn = tk.Button(
        button_frame, 
        text=text, 
        font=("Arial", 16, "bold"), 
        bg=bg_color, 
        fg=fg_color,
        command=lambda t=text: on_button_click(t)
    )
    
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

# Растягиваем ячейки сетки
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Запуск приложения
root.mainloop()
