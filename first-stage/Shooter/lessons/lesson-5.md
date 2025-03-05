# 5 Урок


## Краткое содержание

- Победа игрока
- [Интерфейс](#интерфейсы)
  - Отображение `HP` [игрока](#интерфейсы) 
  - Поражение игрока
  - Меню
  - Победа игрока

## Победа игрока

Игрок победит, если продержится достаточное количество времени. 

Что делаем?
- Добавим `Timer` к корневому узлу, главной сцены игры и можете его переименовать в `GameTimer`
- Выставляем желаемое значение `Wait Time`. Например, 40 секунд
- Ставим `Autostart`
- Присоединяем сигнал `timeout` к скрипту корневой сцены
- Прописываем паузу дерева

#### Скрипт:

```gdscript
# game.gd

func _on_game_timer_timeout():
	print("You win") # выводим надпись
	get_tree().paused = true # ставим дерево на паузу
```

И вот собственно готова механика победы игрока. 

## Интерфейсы
### Интерфейс игрока

Сделаем активное отображение `HP` у игрока. Сделаем мы это при помощи `AnimatedSprite2D`. Создаем `CanvasLayer` в главной сцене и можем его переименовать в `HUD` и внутри этого узла создаем узел `Control`, а уже в него добавляем `AnimatedSprite2D`.

Должно быть что-то вроде этого:

<img src='https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/ui_tree_screenshot.jpg'>

>[!Note]
>`HUD` (Heads-Up Display) — это элемент пользовательского интерфейса в играх, который отображает важную информацию для игрока без прерывания игрового процесса.
>
>Примеры информации на HUD:
>- Здоровье (`HP`), мана, выносливость
>- Очки, счетчик комбо
>- Карта или мини-карта
>- Оружие и боеприпасы
>- Таймер или индикаторы миссии

#### Поработаем с `TextureProgressBar`.

<img src='https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/TextureProgressBar.png'>

- Загружаем в параметры `Under` и `Over` необходимые текстуры
	- в `Under` мы загружаем задний фон прогресс бара
 	- в `Over` соответсвенно текстуру заполненного прогресс бара 
- Параметр `Max Value` должен быть равен максимальному (изначальному) количеству `hp` игрока (если ученик захочет, чтобы у игрока было 100 `hp`, то `Max Value` должен быть равен 100) 


### Скрипт интерфейса

Задаем узлу игрока уникальное имя (жмем <kbd>правой кнопкой мыши</kbd> на узел и ищем знак `%` с текстом `Доступ как к уникальному имени`). Оно нужно, чтобы незавсимо от расположения узла - путь оставался неизменным. 

Пример:

```gdscript
# example

func _process(delta):
	$"../../Player".hp # вместо такого пути
	%Player.hp # будет такой и обратите внимание на знак процента
```

Тепреь создаем скрипт внутри узла `Control` и пишем следующий код:

```gdscript
extends Control


func _process(delta):
	$TextureProgressBar.value = %Player.hp # value прогресс бара равен количеству хп игрока
```

И не забываем поправить количество `hp` у игрока.

```gdscript
# player.gd

var hp = 8 # меняем на нужное количество, например 100
```

## Поражение игрока

На самом деле мы помимо интерфейса еще перепишем код игрока. Нам теперь необходимо, чтобы игрок мог во время проигрыша вызывать интерфейс проигрыша, где будет написано "Ты проиграл" или что-то похожее.

Переделаем скрипт игрока мы таким образом:

```gdscript
signal game_over
var is_dead := false # вводим новую переменную 


func _physics_process(delta):
	if not is_dead: # если игрок не умер, то...
		handle_movement() # вызываем метод обработки движения
		handle_actions() # вызываем метод обработки действий
		take_damage(delta) # вызываем метод получения урона
	
	move_and_slide()


func handle_movement(): # всю логику мы перенесли сюда
	var direction := Input.get_vector("left", "right", "up", "down")
	look_at(get_global_mouse_position())
	if direction != Vector2.ZERO:
		velocity = direction * SPEED
	else:
		velocity = Vector2.ZERO


func handle_actions() -> void: # и сюда
	if Input.is_action_pressed("LMB"):
		shoot()


func take_damage(delta):
	const DAMAGE_RATE = 1
	var overlapping_zombies = %HurtBox.get_overlapping_bodies()
	if overlapping_zombies.size() > 0:
		hp -= DAMAGE_RATE * overlapping_zombies.size() * delta
		if hp <= 0.0:
			is_dead = true # переключаем её, когда игрок проигрывает
			emit_signal("game_over")
```

### Работаем с узлами

- Создаем узел `Control` и называем его `GameOverUI` и делаем его на весь `viewport` (игровой экран). В нем будет `Label` в который мы помещаем текст "Ты проиграл!".
- Крепим от игрока сигнал `game_over`, который находится во вкладке `Узел`, к корневому узлу сцены `Game` (там где у нас уровень).
- Прописываем скрипт для отображения интерфейса

<img src='https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/GameOverUIView.png'>

#### Скрипт узла `Game`

```gdscript
func _on_player_game_over():
	$CanvasLayer/GameOverUI.visible = true
```
## Меню

Теперь поработаем над кнопкой паузы. Вызываться она будет на уже классическую клавишу <kbd>ESC</kbd>. Идея простая:
- Создаем новую сцену, корнем делаем `Control`, можно назвать `PauseMenu`
- Далее создаем `VBoxConatiner` и ставим его по центру
<img src='https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/screenshot_center.jpg'>
- Внутрь `VBoxConatiner` добавляем два `Button`, назвать их можно `ContinueButton` и `ExitButton`. Текст в кнопках пишем соотвествующий
- Добавляем скрипт к `PauseMenu` и туда же присоединим сигналы `pressed` от кнопок

Теперь посмотрим на скрипт:

```gdscript
extends Control

var is_paused := false # переменная, которая проверяет на паузе ли игра


func _ready():
	self.visible = false


func _input(event):
	if Input.is_action_just_pressed("ui_cancel"):
		is_paused = !is_paused
		
	#printerr("Is paused: ", is_paused)
	
	if is_paused:
		self.visible = true
		get_tree().paused = true
	else:
		get_tree().paused = false
		self.visible = false
		


func _on_continue_button_pressed():
	is_paused = false
	get_tree().paused = false
	

func _on_exit_button_pressed():
	get_tree().quit()
```


### Описание
Этот код реализует простое **меню паузы** в игре. 
Меню появляется при нажатии на клавишу <kbd>Esc</kbd> и позволяет либо продолжить игру, либо выйти.

#### Код
```gdscript
extends Control

var is_paused := false

func _ready():
    self.visible = false

func _input(event):
    if Input.is_action_just_pressed("ui_cancel"):
        is_paused = !is_paused
    
    if is_paused:
        self.visible = true
        get_tree().paused = true
    else:
        get_tree().paused = false
        self.visible = false

func _on_continue_button_pressed():
    is_paused = false
    get_tree().paused = false

func _on_exit_button_pressed():
    get_tree().quit()
```

#### Разбор кода
##### 1. **Объявление переменной**
```gdscript
var is_paused := false
```
- Переменная `is_paused` хранит состояние паузы (**`true`** — игра на паузе, **`false`** — игра продолжается).
- В начале (`:= false`) паузы нет.

##### 2. **Функция `_ready()`**
```gdscript
func _ready():
    self.visible = false
```
- Вызывается при загрузке сцены.
- `self.visible = false` скрывает меню паузы в начале игры.

##### 3. **Функция `_input(event)`** – обработка нажатия клавиши
```gdscript
func _input(event):
    if Input.is_action_just_pressed("ui_cancel"):
        is_paused = !is_paused
```
- `Input.is_action_just_pressed("ui_cancel")` проверяет, нажата ли клавиша `ui_cancel` (обычно **Esc**).
- `is_paused = !is_paused` переключает паузу (`true` → `false`, `false` → `true`).

##### 4. **Включение и выключение паузы**
```gdscript
if is_paused:
    self.visible = true
    get_tree().paused = true
else:
    get_tree().paused = false
    self.visible = false
```
- **Если `is_paused == true` (пауза включена)**:
  - `self.visible = true` – показать меню паузы.
  - `get_tree().paused = true` – остановить игру (враги, анимации, физика).
- **Если `is_paused == false` (пауза выключена)**:
  - `get_tree().paused = false` – возобновить игру.
  - `self.visible = false` – скрыть меню паузы.

##### 5. **Кнопка "Продолжить"**
```gdscript
func _on_continue_button_pressed():
    is_paused = false
    get_tree().paused = false
```
- Вызывается при нажатии кнопки **"Продолжить"**.
- Выключает паузу и возобновляет игру.

##### 6. **Кнопка "Выход"**
```gdscript
func _on_exit_button_pressed():
    get_tree().quit()
```
- Закрывает игру.

---
💡 **Дополнительно**:
- Можно добавить **анимацию** появления меню.
- Можно сделать **плавное затемнение** фона при паузе.
- Можно добавить **горячие клавиши** для выхода из игры.

#### Теперь по порядку

Начинаем мы с сигналов, которые идут от кнопок. Их надо подключить

```gdscript
func _on_continue_button_pressed():
	pass
	

func _on_exit_button_pressed():
	pass
```

Далее создаем переменную `is_paused := false` и в принципе можно написать код, чтобы меню паузы изначально было невидимым.
Теперь при нажатии на кнопку `ContinueButton` мы переключаем значение переменной `is_paused` в `false`

```gdscript
func _on_continue_button_pressed():
	is_paused = false
	get_tree().paused = false # также мы ставим дерево на паузу
```
А в сигнале, который идет от кнопки `ExitButton` пишем следующее:

```gdscript
func _on_exit_button_pressed():
	get_tree().quit() # выходим из игры
```

И теперь самая интересная часть. Мы тут делаем выключение паузы на <kbd>ESC</kbd>. Нажатие на кнопку паузы включает и выключает саму паузу

```gdscript
func _input(event):
	if Input.is_action_just_pressed("ui_cancel"):
		is_paused = !is_paused
		
	if is_paused:
		self.visible = true
		get_tree().paused = true
	else:
		get_tree().paused = false
		self.visible = false
```

>[!Caution]
>В инспкторе, во вкладке `Process` у кнопок надо переключить параметр `Mode` на значение `Always`, чтобы кнопка работала даже если дерево на паузе.
