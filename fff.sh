#!/bin/bash

# 1. Установка sqlite3
echo "Установка sqlite3..."
sudo apt update && sudo apt install sqlite3 -y

# 2. Создание БД и таблицы, 3. Выполнение INSERT и SELECT
echo "Создание базы данных и выполнение запросов..."
sqlite3 students.db <<EOF
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
);

INSERT INTO students (name, age, grade) VALUES 
('Иван Иванов', 20, 'A'),
('Мария Петрова', 21, 'B'),
('Алексей Смирнов', 19, 'A');

.mode column
.headers on
SELECT * FROM students;
EOF

echo "Готово! База данных students.db создана."
