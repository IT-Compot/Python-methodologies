# КосмоШутер | Урок 1

(краткое описание проекта)

## Демонстрация проекта

Суть игры - (описать в чём смысл): 

(гифка готового проекта)

## Содержание

(содержание)

## План на занятие 

(что будем делать конкретно сегодня)\
\
Начнём!

### Создание проекта

Как обычно создаём новый проект, называем его КосмоШутер:

![1](https://github.com/user-attachments/assets/731f1c13-aa82-4ef9-b9fa-d25410923f92)

Выбираем 3D сцену:

![image](https://github.com/user-attachments/assets/920c1f72-9163-4b65-a885-0960fbc45ec9)

Переименуем сцену и назовём её `game` (для нашего удобства):

![image](https://github.com/user-attachments/assets/fb4f299d-98e2-4888-a921-c98b03c48d93)

### Делаем окружение, космос

На этом занятии будем создавать реалистичную сцену космоса, поэтому подгрузим в движок картинку космоса (можно скачать в интернете):

![image](https://github.com/user-attachments/assets/aa06b9bf-bf5e-4b77-87a2-5269edcb2625)

Результат:

![image](https://github.com/user-attachments/assets/947c1ea7-de07-4678-a29b-3615fa5363c3)

Теперь прикрепим к `Node3D`, которая теперь называется `game`, узел `WorldEnvironment`:

![2](https://github.com/user-attachments/assets/c12bdd76-1fe3-4585-aeec-08212b8f812b)

А теперь переходим к настройке данного узла, переходим в правую часть экрана, в инспектор, видим там параметр `Environment`, задаём ему `Environment`:

![3](https://github.com/user-attachments/assets/95136982-3c88-4dbb-9874-0a46dff9b3d3)

И настраиваем окружение `Environment`, выбираем вкладку `Background`, в ней в параметре `Mode` выбираем вариант `Sky`, после чего появится вкладка `Sky` ниже. До этих действий её там не будет.

![5](https://github.com/user-attachments/assets/478ac670-1272-4654-873b-45bf2fcfe21b)

И теперь настраиваем небо, тыкаем на окошко параметра `Sky`, выбираем `Создать Sky` кликаем на то же окошко, где появилось слово `Sky`, сразу у нас есть новое окошко снизу в параметре `Sky Material`, там же выбираем `PanoramaSkyMaterial`:

![6](https://github.com/user-attachments/assets/807c3471-6221-4f29-92c3-029f96e2d950)

Мы видим тут параметр `Panorama`, в котором пусто, перетягиваем туда файлик со звёздным небом (из левой части экрана, гед находится файловая система):

![image](https://github.com/user-attachments/assets/50e4abb7-529f-4d83-9445-17e73c119ff4)

Результат:

![image](https://github.com/user-attachments/assets/a88cec3e-8219-42c2-9c9b-162993973a4c)

Теперь настроим внешний вид неба, на гифки видны основные параметры, которые мы можем настроить, но можно поробовать и остальные.

![7](https://github.com/user-attachments/assets/8ed0c38e-3204-4290-9e90-ca5c234e42ee)

На этом закончим с настройкой неба и приступим к космическому кораблю.

### Делаем космический корабль

Корабль мы тоже будем искать в интернете, в этом нам очень поможет сайт Sketchfab (ссылку сюда вставить):

![image](https://github.com/user-attachments/assets/d125944f-6f01-437d-8d3d-202f3b5cd7e9)

Вот мы нашли понравившийся нам корабль, справа у него есть иконка ![image](https://github.com/user-attachments/assets/82be4ecc-6c83-428c-b000-f42bc335343e), заходим на страницу этой 3D модели, находим кнопку `Download 3D model` и выбираем формат `glTF`:

![8](https://github.com/user-attachments/assets/defc2ade-d700-45bf-9055-0e3a405102b6)


