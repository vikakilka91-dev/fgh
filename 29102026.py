import tkinter as tk

class Interface:
    def __init__(self):
        # Создаем главный объект root
        self.root = tk.Tk()
        
        # Настройки компонента root (Пункт 5)
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        self.root.configure(bg="#2d2d2d")

        # --- Элементы интерфейса ---
        
        # Заголовок
        label = tk.Label(self.root, text="Мой Таск-Менеджер", font=("Arial", 16, "bold"), bg="#2d2d2d", fg="white")
        label.pack(pady=15)

        # Поле ввода
        self.entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.entry.pack(pady=5)

        # Кнопка добавления
        self.btn_add = tk.Button(self.root, text="Добавить задачу", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=self.add_task)
        self.btn_add.pack(pady=10)

        # Кнопка удаления
        self.btn_del = tk.Button(self.root, text="Удалить выбранное", font=("Arial", 10), bg="#f44336", fg="white", command=self.delete_task)
        self.btn_del.pack(pady=5)

        # Список задач
        self.listbox = tk.Listbox(self.root, font=("Arial", 12), width=35, height=12)
        self.listbox.pack(pady=15)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except IndexError:
            pass

    def run(self):
        self.root.mainloop()

# --- Запуск приложения ---
if __name__ == "__main__":
    app = Interface()
    app.run()
