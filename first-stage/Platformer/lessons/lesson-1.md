# Урок 1

## Краткое содержание
- Создание персонажа
- Создание тестовой карты

## Создание персонажа
### Подготовка сцены
- Создаем новую сцену и нажимаем `Другой узел`. В основе сцены персонажа лежит узел `CharacterBody2D` и переименуем его в `Player`.
- Создаем дочерние узлы: `AnimatedSprite2D`, `CollisionShape2D`

Должно получиться это: 

<img width="200" height="138" alt="image" src="https://github.com/user-attachments/assets/e7f6d183-0eae-41b6-890f-2fbcf6d75c72" />

Сохраняем сцену

### Работа с узлами

В `AnimatedSprite2D` в `Инспекторе` открываем вкладу `Animation` и в параметре `Sprite Frames` нажимаем на: `Новый SpriteFrames`, таким образом мы создали новый ресурс. Открываем его, нажатием на созданный `SpriteFrames`.
Теперь создаем три базовые анимации для нашего игрока: 
- `idle` - стоять
- `run` - бежать
- `jump` - прыгать

Создается новая анимация следующим образом: 
<img width="1488" height="271" alt="image" src="https://github.com/user-attachments/assets/e83e6213-f0c7-4fec-9e42-9c069b4b3446" />

и получается это:

<img width="211" height="274" alt="image" src="https://github.com/user-attachments/assets/6e574c81-a855-45dd-ba85-0cd3f87d3261" />
