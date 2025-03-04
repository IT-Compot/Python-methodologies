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
