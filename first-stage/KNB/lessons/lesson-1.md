# КНБ



## Краткое содержание
- Создаем интерфейс игры
- Добавляем код выбора игрока и бота

## Создание интерфейса игры

#### Базовая структура сцены
```
Game (Node2D)  
├── Background (Sprite2D)  
├── PlayerAnimation (AnimatedSprite2D)  
├── BotAnimation (AnimatedSprite2D)  
├── ButtonPaper (Button)  
├── ButtonRock (Button)  
└── ButtonScissors (Button)
```
Перетащите фон на сцену игры (ученики могут поставить свой фон при желании), растяните по ширине `viewport`.

#### Параметры `AnimatedSprite2D`

| Параметр          | Игрок (`PlayerAnimation`)                     | Бот (`BotAnimation`)                          |
|-------------------|------------------------------------------|------------------------------------------|
| **SpriteFrames**  | `New SpriteFrames` с анимациями:         | `New SpriteFrames` с анимациями:         |
|                   | - rock_animation                         | - rock_animation                         |
|                   | - scissors_animation                     | - scissors_animation                     |
|                   | - paper_animation                        | - paper_animation                        |
| **Animation**     | Любая из:                                | Любая из:                                |
|                   | - rock_animation                         | - rock_animation                         |
|                   | - scissors_animation                     | - scissors_animation                     |
|                   | - paper_animation                        | - paper_animation                        |
| **Flip_h**        | `false` (отключен)                       | `true` (включен, если бот справа)        |
| **Modulate**        | можно оставить стандартный                       | покрасить в любой другой цвет       |


>[!Note]
>`flip_h` для бота:
>   - Включается только если бот расположен справа от игрока
>   - Необходим для зеркального отображения спрайта


#### Параметры `Button`

# Параметры кнопок управления

| Параметр          | Камень (`ButtonRock`)          | Ножницы (`ButtonScissors`)    | Бумага (`ButtonPaper`)        |
|-------------------|--------------------------|--------------------------|--------------------------|
| **Icon**          | `res://assets/rock.png` (зависит от вашего пути, будет показано изображение ассета)  | `res://assets/scissors.png` | `res://assets/paper.png` |
| **Expand Icon**   | `true`                   | `true`                   | `true`                   |
| **Flat**          | `true` (чтобы убрать фон, опционально)      | `true`                   | `true`                   |



Должно получиться что-то похожее на это:

![image](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/KNB/Assets/game_screen.png)
