import tkinter as tk
import math

root = tk.Tk()
root.geometry("450x450")
root.title("Круглый узор - Урок 10")

# Массив с цифрами для кнопок (от 0 до 9)
numbers = [str(i) for i in range(10)]

# Параметры для расположения по кругу
center_x, center_y = 225, 225 # Центр окна
radius = 150                  # Радиус круга
i = 0                         # Счетчик для цикла while

# --- Пункт 5: Использовать только цикл while и не более одной условной конструкции if ---
while i < len(numbers):
    # --- Пункт 3: Алгоритм расстановки в виде круга ---
    # Вычисляем угол для каждой кнопки (360 градусов / 10 кнопок = 36 градусов)
    angle = math.radians(i * 36)
    
    # Вычисляем координаты X и Y по формулам тригонометрии
    x = center_x + radius * math.cos(angle) - 25 # -25 для центрирования самой кнопки
    y = center_y + radius * math.sin(angle) - 25
    
    # Создаем кнопку и размещаем её по абсолютным координатам (place)
    # Пункт 4: Минимальное количество строк (все делаем в одной строке)
    btn = tk.Button(root, text=numbers[i], font=("Arial", 12, "bold"), bg="#ffcc00", width=4, height=2)
    btn.place(x=x, y=y)
    
    # --- Единственный if в программе ---
    # Если дошли до последней кнопки (цифры 9), добавляем в центр кнопку "Очистить" (C)
    if i == len(numbers) - 1:
        tk.Button(root, text="C", font=("Arial", 12, "bold"), bg="#ff6666", command=lambda: [b.destroy() for b in root.winfo_children() if isinstance(b, tk.Button)]).place(x=center_x-25, y=center_y-25, width=50, height=50)
    
    i += 1 # Увеличиваем счетчик

root.mainloop()
