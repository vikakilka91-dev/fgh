import tkinter as tk

def create_app():
    # Пункт 3: экземпляр Tk
    root = tk.Tk()

    # Пункт 5: Размер, имя, иконка
    root.geometry("400x300")
    root.title("Урок 8 - Tkinter")
    # root.iconbitmap('icon.ico') # Раскомментируйте, если есть файл иконки в папке

    # Пункт 4: Label и Button
    label = tk.Label(root, text="Добро пожаловать!", font=("Arial", 14))
    label.pack(pady=20)

    button = tk.Button(root, text="Нажми меня", command=root.destroy) # Кнопка закрытия
    button.pack(pady=10)

    # Пункт 6: mainloop
    root.mainloop()

if __name__ == "__main__":
    create_app()
