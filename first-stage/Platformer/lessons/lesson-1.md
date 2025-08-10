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

В каждую из анимаций добавляем кадры анимаций из спрайт-листа, который лежит у учеников в файловой системе. Чтобы добавить кадры надо нажать на эту кнопку:

<img width="617" height="72" alt="image" src="https://github.com/user-attachments/assets/2205a82f-8326-41d7-9280-d348abfaa6a5" />

Далее выбираем понравившийся ассет и открываем его. Будет что-то на подобии этого:

<img width="1241" height="733" alt="image" src="https://github.com/user-attachments/assets/424b7d39-60dc-4f13-bb42-f5df8e9e56f0" />

В зависимости от выбранного ассета (если вы используете другие) нужно настроить сетку. В одной клетке - один кадр анимации. Вот пример ниже:

<img width="1238" height="729" alt="image" src="https://github.com/user-attachments/assets/bd398b86-acae-45f7-b564-e226936fe66c" />

Теперь в зависимости от анимации, которую вы настраиваете - выбираем необходимые кадры.

`idle`: 

<img width="658" height="328" alt="image" src="https://github.com/user-attachments/assets/40bebb9d-112c-4f39-9951-4e10c90a54b0" />

`jump`:

<img width="638" height="315" alt="image" src="https://github.com/user-attachments/assets/4cde049f-00a2-4785-9a11-e1ac5267dec9" />

`run`:

<img width="727" height="297" alt="image" src="https://github.com/user-attachments/assets/2c8c8b3b-fc9f-483a-a5a9-252cf09b598f" />

>[!Warning]
>Все сильно зависит от ваших ассетов, будьте внимательны! Если вы выбрали предоставленные, то достаточно делать по инструкции.


И вот теперь у нас есть спрайт персонажа! 

<img width="662" height="355" alt="image" src="https://github.com/user-attachments/assets/a0836965-48f6-4299-8aed-6343fcabc964" />

Пора добавить коллизии. Объясните ученикам для чего нужны коллизии. 
Чтобы создать коллизию надо выбрать `CollisionShape2D` и в `Инспекторе` выбрать параметр `Shape`, создать ресурс `CapsuleShape2D` и подогнать под размеры персонажа. Рекомендуется настроить таким образом, чтобы коллизия заканчивалась у ног персонажа, нужно это для того, чтобы ноги визуально касались земли.

<img width="774" height="757" alt="image" src="https://github.com/user-attachments/assets/6c7a62fd-b2ae-4d5d-970c-28bc5b449016" />

