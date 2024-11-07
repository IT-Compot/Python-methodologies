# Царь горы | Урок 1

Первый проект в 3D.\
В этом проекте впервые поработаем с 3D фигурами, научимся добавлять их на сцену, настраивать их коллизию и напишем первый скрипт для 3D игры.

## Демонстрация проекта

Суть игры - столкнуть всех ботов с платформы в пропасть за отведённое количество времени: 

![7](https://github.com/user-attachments/assets/b0731a36-9613-48d4-9790-66a0d4c93350)

## Содержание

- [План на занятие](#План-на-занятие)
  - [Создание проекта](#Создание-проекта)
    - [Настроим платформу для игры](#Настроим-платформу-для-игры)
    - [Создание персонажа](#Создание-персонажа)
    - [Камера и окружение](#Камера-и-окружение)
    - [Персонаж и фон](#персонаж-и-фон)
  - [Допы](#Допы)
    - [Горячие клавиши для работы со сценой](#Горячие-клавиши-для-работы-со-сценой)
    - [Текстуры для объектов на сцене](#Текстуры-для-объектов-на-сцене)
    - [Свои клавиши управления](#Свои-клавиши-управления)
    - [Статичная камера](#Статичная-камера)


## План на занятие 

На первом занятии подготовим сцену и персонажей, к концу занятия персонаж сможет сталкивать ботов с платформы, но пока ничего не происходит.\
\
Начнём!

### Создание проекта

Как обычно создаём новый проект, называем его Царь горы:

![gif1](https://github.com/user-attachments/assets/7a5b2550-0278-409b-844e-00d2691ee5d0)

На этот раз создаём 3D сцену:

<p align="center">
  <img width="577" height="422" src="https://github.com/user-attachments/assets/b2a44007-65d1-4e57-b512-ce43d47f2b0c">
</p>

>[!TIP]
> Если мы будем сталкивать врагов, что нам для этого понадобится добавить на сцену?

Добавим платформу, узел называется `MeshInstance3D`:

![3](https://github.com/user-attachments/assets/79555ea2-d49b-4e46-8574-da913e51dbea)

> [!IMPORTANT]
> Что такое Меш? По-английский переводится как `сетчатый`, `ячеистый`. В 3D моделировании `Mesh` набор вершин и многоугольников, определяющих форму трёхмерного объекта, поэтому такое название.

### Настроим платформу для игры

Выберем простую и плоскую сверху фигуру, например, куб:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/c9c31f83-186a-40df-97e0-c0c10ad34668">
</p>

Настроим его. По умолчанию у нас появляется куб 1 на 1 метр.

Сделаем его чутка побольше, чтобы нам хватило пространства для игры.
Нажмём на значок  <sub>![бэ](https://github.com/user-attachments/assets/63104398-fa87-4cec-b3cd-2b761d65ca3a)</sub>, чтобы значения в окошках не привязывались друг к другу и были независимыми:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/4083de8b-6361-4c08-ad01-17af6fd8b27a">
</p>

Пусть по `Y` останется единичка, а по `X` и `Z` выставим значения побольше.

По итогу имеем такую платформу:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/b86a1da4-85ba-4e0c-8a63-e52b0591c4d4">
</p>

>[!TIP]
> Что нужно добавить платформе, чтобы герой не проваливался сквозь неё?

Добавим платформе коллизию, делается это следующим образом:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/e22977b8-cdf7-4ab2-a061-22c490a05f6a">
</p>

На этом сцена готова, можно приступать к персонажу.

### Создание персонажа

>[!TIP]
> Нужно ли персонажу заранее создавать узел в дереве сцены? Какой это будет узел?

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/7a8c0b94-af12-4626-9746-42f8f4425158">
</p>

Персонаж у нас тоже теперь в 3D, и поэтому для него мы добавим дочерний узел `MeshInstance3D`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/1bab0c67-7a83-4fe8-805c-718770a91975">
</p>

Настроим его в правой части экрана, выберем `CapsuleMesh`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/cc831fa6-b615-4b8d-b4dc-96d4b0066e5f">
</p>

В трансформе поднимем его на 1 метр:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/0a773b8c-504e-4d85-b309-2c6ad58f8a1f">
</p>

>[!TIP]
> Внешний вид персонажа готов, что ещё ему необходимо добавить? Будет ли он сейчас стоять на платформе или провалится?

Ему нужна коллизия. Добавим её, узел называется `CollisionShape3D`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/1b68d0ff-f841-48d8-8231-8d7c3811caac">
</p>

Аналогично настраиваем `CollisionShape3D`, настраиваем форму и поднимаем на 1 метр:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/bd32b278-eb4d-4639-8b4e-94965438b889">
</p>

Отлично, персонаж полностью готов.

### Камера и окружение

>[!TIP]
> Мы будем наблюдать за процессов игры со стороны, значит какой узел нам ещё понадобится?

Это `Camera3D`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/dae6b408-6687-4ee1-8b8e-6149651d0a72">
</p>

Поставим камеру на сцену, чтобы она смотрела на персонажа:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/871bc2ed-6037-4d00-ada2-214544a33625">
</p>

Запускаем игру и видим, что всё серое:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/6b08e48a-2034-4667-9bbc-af336519c4e3">
</p>

Это связано с освещением сцены. Давайте его изменим, найдём три точки на верхней панели:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/ba23d6a0-7743-41a9-b6fe-2559ca892ab8">
</p>

Обязательно нажмём на кнопку `Добавить окружение к сцене`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/f66d7885-fe39-47ff-b3ff-32279099207c">
</p>

Слева в узлах сцены появится новый узел `WorldEnvironment`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/2e6442e1-1c42-4ea4-a084-68c57963cb76">
</p>

Через ту же вернхнюю панель можно добавить в сцену солнце:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/56368a7b-fe31-4f09-8aba-3d408d739f6c">
</p>

Окружение мира готово, можно приступать к написанию скрипта.

### Скрипт персонажа

Персонажа можно переименовать и прикрепить к нему готовый скрипт из предложенного шаблона:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/247c29ab-b29b-4902-a100-82d195c130d1">
</p>

На этом базовая часть проекта готова, персонажем можно уже сейчас управлять на стрелочки и он может упасть с платформы.

## Допы

### Горячие клавиши для работы со сценой

а

### Текстуры для объектов на сцене

Покрасим и поменяем цвет и текстуры персонажей в игре. Начнём с платформы. Изменить текстуру можно перетягиванием любой картинки из фаловой системы на желаемый объект:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/ccfdb9be-1cd7-43f2-83ab-bc66c9486823">
</p>

Настроить внешний вид объекта можно и без подгрузки текстуры:

![image](https://github.com/user-attachments/assets/18603817-066c-4c9e-a553-be21c22181a6)

Осталось только настроить внешний вид бота, сделаем ему забавный вид иконки `Godot`, обязательно выберем `MeshInstance3D` нашего бота на сцене:

![4](https://github.com/user-attachments/assets/b19118b9-5c2d-40f5-a4bc-57e4100e02e0)

Далее перейдём сразу в его инспектор и во вкладке `Geometry` зададим ему материал:

![5](https://github.com/user-attachments/assets/778db3df-ee28-4117-a066-f8e82fc681b2)

И настроим его параметр `UV1`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/0073c35c-d6b1-4fbd-a81a-c4c52cd069e9">
</p>

Тогда картинки перераспределятся по поверхности меша.

### Свои клавиши управления

В движке многие кнопки уже настроены по умолчанию, прикрепим к дефолтным кнопкам классические W-A-S-D:

![10](https://github.com/user-attachments/assets/238269ff-c1b2-4fbe-8d14-4563a478b077)

Теперь персонаж ходит и на стрелочки и на W-A-S-D.

### Статичная камера

Камера будет статично смотреть на сцену, если она прикреплена к `Node3D`:

<p align="center">
  <img width="" height="" src="https://github.com/user-attachments/assets/bcac48f3-2eac-4328-9a85-61b1d0f58b2b">
</p>

И, естественно, будет следовать за персонажем, если прикреплена к его узлу.




























