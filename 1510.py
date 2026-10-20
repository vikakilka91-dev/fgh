import os
import sys

# --- Пункт 1: Создайте функцию get_base_dir() чтобы получать текущую папку запуска ---
def get_base_dir():
    """
    Возвращает абсолютный путь к папке, где находится исполняемый файл.
    Если приложение запущено как скрипт .py, возвращает папку скрипта.
    Если как .exe (после сборки pyinstaller), возвращает папку с .exe.
    """
    if getattr(sys, 'frozen', False):
        # Если запущено как скомпилированный exe файл
        base_dir = os.path.dirname(sys.executable)
    else:
        # Если запущено как обычный python скрипт
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return base_dir


# --- Пункт 2: Создайте функцию insure_save_file() для создания файла сохранений при первом запуске ---
def insure_save_file():
    """
    Проверяет наличие файла сохранения. Если его нет — создает пустой файл.
    """
    # Получаем путь к папке запуска
    base_path = get_base_dir()
    
    # Путь к файлу сохранения (можно назвать save_data.txt или data.json)
    file_path = os.path.join(base_path, "save_data.txt")
    
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        # Если файла нет, создаем его в режиме записи 'w'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("Сохранения созданы.\n") # Можно записать начальные данные
        print(f"Файл сохранения создан по пути: {file_path}")
    else:
        print(f"Файл сохранения уже существует: {file_path}")

# Пример использования (для проверки работы кода)
if __name__ == "__main__":
    print("Запуск приложения...")
    # Вызываем функцию при старте программы
    insure_save_file()
    
    # --- Здесь должен быть код вашего Tkinter интерфейса ---
    # import tkinter as tk
    # root = tk.Tk()
    # ...
    # root.mainloop()
    print("Готово.")
