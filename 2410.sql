-- 1. Создаем базу данных (схему)
CREATE DATABASE IF NOT EXISTS Academy;
USE Academy;

-- 2. Создаем первые 4 таблицы (без внешних ключей или с внутренними связями)
-- Эти таблицы создаются первыми, так как на них будут ссылаться другие.

CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE student_group (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Таблица оценок ссылается на студентов (студенты будут созданы позже, 
-- поэтому FK на них добавим отдельно в конце, либо создадим таблицу студентов раньше.
-- В рамках задания мы просто создаем структуру, порядок может быть любым, 
-- если мы используем ALTER TABLE для добавления FK).

CREATE TABLE student_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT,
    date_received DATE,
    -- Внешний ключ на предметы (subject_id -> subjects.id)
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- 3. Создаем оставшиеся 4 таблицы (с внешними ключами)

CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    group_id INT,
    -- Внешний ключ на группы (group_id -> student_group.id)
    FOREIGN KEY (group_id) REFERENCES student_group(id) ON DELETE SET NULL
);

-- Добавляем внешний ключ к student_grades, так как таблица students теперь создана
ALTER TABLE student_grades
ADD CONSTRAINT fk_student_grades_student
FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE;

CREATE TABLE lessons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT,
    teacher_id INT,
    class_id INT,
    -- Внешние ключи
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE SET NULL,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

CREATE TABLE schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_id INT,
    date_time DATETIME NOT NULL,
    room VARCHAR(20),
    -- Внешний ключ на уроки
    FOREIGN KEY (lesson_id) REFERENCES lessons(id) ON DELETE CASCADE
);

-- 4. Скрипт для сдачи (проверка)
-- Выводим список всех созданных таблиц в базе Academy
SHOW TABLES;
