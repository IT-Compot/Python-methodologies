# Файтинг | Урок 1

(описание проекта)

## Демонстрация проекта

(суть игры)\
\
(гифка)

## Содержание

(содержание)

## План на занятие 

На первом занятии сделаем то-то\
\
Начнём!

### Создание проекта

Как обычно создаём новый проект, называем его Файтинг:

![image](https://github.com/user-attachments/assets/35baff73-2817-4b7d-b564-a5c4ce903664)

### Создание и настройка карты

Для проекта файтинга нам понадобится готовая карта, скачаем её на Scetchfab в формате glTF:

![image](https://github.com/user-attachments/assets/a18d84e2-e9b8-40cf-8aec-86c5139d3639)

После того, как карта скачается, открываем папку проекта в проводнике:

![image](https://github.com/user-attachments/assets/cde03df1-8779-41f7-bd14-255ebb3251ab)

Нам нужно два окна, создадим в папке проекта ещё одну папку, назовём её `map`, `карта`, и перенесём туда файлы из архиватора:

![1](https://github.com/user-attachments/assets/5625a95a-bdce-4447-9223-075590e4c88a)

Далее откроем импортированную карту следующим образом:

![image](https://github.com/user-attachments/assets/4a04b348-63ab-4df7-80f7-0c375d43dd7a)

И чтобы редактировать (добавлять коллизии), откроем её отдельной сценой в движке:

![2](https://github.com/user-attachments/assets/22fc4543-87b8-4f06-9b7a-d643b1180a0f)

Добавим в сцену карты `StaticBody3D` и прикрепим к ней 3 узла `CollisionShape3D` (для пола и двух стен, ограничивающих карту):

![3](https://github.com/user-attachments/assets/bae5bf76-62fe-4723-8e7d-1b836d853615)

Затем настроим их:

![image](https://github.com/user-attachments/assets/0a1b0361-88f7-4b3e-bbe8-293caaa4f31f)

Карта с коллизиями готова. Теперь позаботимся о персонаже.

### Персонаж

Персонажа мы скачаем из интернета, в этом нам поможет сайт `Mixamo`. Заходим и ищем подходящего персонажа.

![image](https://github.com/user-attachments/assets/97f7b7bb-fa8f-4f8b-80a3-f0367ff4cdfb)



