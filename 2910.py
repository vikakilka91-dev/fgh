# Пункт 1: Исследование (мы используем классы для создания UI элементов)

# Пункт 3: Создаем один родительский класс по теме (например, базовое окно приложения)
class BaseWindow:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

    # Пункт 4: В родительском классе реализуйте два метода
    def get_info(self):
        """Метод 1: Возвращает информацию об окне"""
        return f"Окно '{self.title}' размером {self.width}x{self.height}"

    def draw(self):
        """Метод 2: Имитация отрисовки окна"""
        return "Отрисовка базового окна (пустой белый экран)..."


# Пункт 4: Создайте два наследника ранее созданного класса родителя
class MainMenuWindow(BaseWindow):
    def __init__(self, title, width, height):
        super().__init__(title, width, height) # Наследуем свойства
        self.buttons = ["Играть", "Настройки", "Выход"]

    # Пункт 5: В классах наследников переопределите методы, созданные в родительском классе
    def draw(self):
        """Переопределяем метод draw для главного меню"""
        base_draw = super().draw() # Вызываем родительский метод (опционально)
        return f"{base_draw}\nНо здесь мы рисуем кнопки: {', '.join(self.buttons)}"

    def get_info(self):
        """Переопределяем метод get_info"""
        return f"Главное меню '{self.title}'. Кнопок на экране: {len(self.buttons)}"


class GameWindow(BaseWindow):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.player_health = 100

    # Пункт 5: Переопределяем методы
    def draw(self):
        """Переопределяем метод draw для игрового процесса"""
        return f"Загрузка текстур... Отрисовка персонажа. Здоровье: {self.player_health} HP."

    def get_info(self):
        return f"Игровое окно '{self.title}' (Разрешение: {self.width}x{self.height})"


# --- Блок проверки работы программы ---
if __name__ == "__main__":
    print("--- Создание объектов и проверка методов ---\n")

    # Создаем экземпляры классов
    base_win = BaseWindow("Системное окно", 800, 600)
    menu_win = MainMenuWindow("Главное меню игры", 1920, 1080)
    game_win = GameWindow("Уровень 1: Лес", 1920, 1080)

    # Проверяем родительский класс
    print("1. Базовый класс:")
    print(base_win.get_info())
    print(base_win.draw())
    print("-" * 30)

    # Проверяем первого наследника (переопределенные методы)
    print("2. Наследник 1 (Меню):")
    print(menu_win.get_info()) # Вызовет переопределенный метод
    print(menu_win.draw())     # Вызовет переопределенный метод
    print("-" * 30)

    # Проверяем второго наследника (переопределенные методы)
    print("3. Наследник 2 (Игра):")
    print(game_win.get_info())
    print(game_win.draw())
