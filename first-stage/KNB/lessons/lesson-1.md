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


## Код

Прикрепляем скрипт к корневому узлу. Добавляем сигналы `pressed` от кнопок к скрипту и получаем следующий код:

```gdscript
func _on_button_paper_pressed():
	pass


func _on_button_rock_pressed():
	pass


func _on_button_scissors_pressed():
	pass
```

Теперь создаем переменные, одна из которых будет хранить значения выбранные игроком, а вторая является ссылкой на узел с анимацией игрока

```gdscript
var player := "" # значения:  "paper", "rock", "scissors"
@onready var player_animation = $PlayerAnimation
```

И переписываем скрипт:

```gdscript
func _on_button_paper_pressed():
	player = "paper" # меняем значение на бумагу
	player_animation.play("paper_animation") # меняем анимацию


func _on_button_rock_pressed():
	player = "rock" # камень
	player_animation.play("rock_animation")



func _on_button_scissors_pressed():
	player = "scissors" # ножницы
	player_animation.play("scissors_animation")

```

### Код бота

Здесь код можете переписывать сверху вниз

```gdscript
func bot_choice():
	var number = 0 # переменная с номером
	number = randi() % 3 # генерация случайного числа от 0 до 2
	print(number)

	# логика выбора на основе случайного числа:
	if number == 0:
		bot = "paper" # запись выбора в переменную
		bot_animation.play("paper_animation") # проигрывание анимации
	if number == 1:
		bot = "rock"
		bot_animation.play("rock_animation")
	if number == 2:
		bot_animation.play("scissors_animation")
		bot = "scissors"
```

<details>
	<summary>Про randomize() </summary>
	
### Уточнение о работе `randomize()` в `Godot`

#### Фактическое поведение в современных версиях `Godot (4.0+)`

1. **Автоматическая инициализация**:
   - Начиная с `Godot 4.0`, движок **автоматически вызывает `randomize()`** при запуске проекта
   - Это было сделано для упрощения разработки

2. **Почему ваш код работает без `randomize`**:
   - Даже без явного вызова `randomize()` вы получаете разные последовательности
   - `Godot` сам устанавливает `seed` на основе системного времени

3. **Остающиеся рекомендации**:

```gdscript
# Лучшая практика (для совместимости и явного контроля)
func _ready():
    randomize()  # Явная инициализация
```

>[!Tip]
>Можете дополнительно рассказать про это ученикам и явно указать `randomzie()` в коде
</details>
