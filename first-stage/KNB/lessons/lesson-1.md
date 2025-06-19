# КНБ

![hippo](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/KNB/Assets/KNB.gif)

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
Должно получиться что-то похожее на это:

![image](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/KNB/Assets/game_screen.png)
