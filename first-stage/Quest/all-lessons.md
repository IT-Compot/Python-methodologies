# Quest
Проект, направлен на отработку тем, изученных на предыдущих уроках. В ходе создания игры ученики закрепят концепции объектно-ориентированного программирования (ООП) и научатся применять их на практике.

## Цели
- Поработать над генерацией объектов на сцене
- Освоить уже полноценно циклы (ребята по итогу должны по аналогии сами сделать часть кода)
- Это последний проект в 1 году обучения, соответственно ребята показывают свой максимум приобретенных знаний

## Краткое содержание
- Урок 1 - [Карта, игрок](#урок-1)
- Урок 2 - [Боты](#урок-2)
- Урок 3 - (Квест)
- Урок 4 - (Доработка квеста)
- Урок 5 - 
- Урок 6 - 
- Урок 7 - 
- Урок 8 - 




## Урок 3

Этот урок мы начнем с создания NPC который будет выдавать нам задание найти объект. Структура NPC следующая

![image](https://github.com/Sindikaty/byteschool/assets/158248099/7e395b2a-b1c2-4bf8-902d-d73bc5410e1d)

Создаем скрипт у Area2D и создаем следующие переменные

```gdscript
var task = 0;
var task_accept = false
```

Сначала добавим появлени и исчезновение диалога с NPC при входе в зону

```gdscript
func _on_guild_of_heroes_body_entered(body):
	if body.name == "Player":
		$Label_quest.visible = true
		$Button.visible = true

func _on_guild_of_heroes_body_exited(body):
	if body.name == "Player":
		$Label_quest.visible = false
		$Button.visible = false
```

В ранее созданном глобальном скрипте доьбавим список в который мы будем добавлять и удалять задания


```gdscript
var tasks = []

func add_task(task):
	tasks.append(task)

func remove_task(task):
	tasks.erase(task)
```

Также нам нужно создать само яблоко, оно состоит из следующих узлов

![image](https://github.com/Sindikaty/byteschool/assets/158248099/82c99238-e46e-4a22-ad08-9c4d251496eb)

Еще можно создать список текущих квестов, по сути это просто Label в который мы будем вносить текст

![image](https://github.com/Sindikaty/byteschool/assets/158248099/6a16229d-fb1c-433c-9626-17b97de5429b)

Возвращаемся к скрипту зоны. Присоединяем сигнал к кнопке 

```gdscript
func _on_Button_pressed():
	task_accept = true
	$Label_quest.visible = false
	$Button.visible = false
	$"../../CanvasLayer/Quest_list/RichTextLabel".text += "Волшебное яблоко"
	Quest.add_task(task)
	#print("Current quest is: ", task)
	task = 1
	$"../Apple_point".visible = true
```

Теперь у нас на карте появляется яблоко которое нам нужно найти. Добавим у него сигнал при входе в него

```gdscript
func _on_Apple_point_body_entered(body):
	if body.name == "Player":
		if task == 1:
			$"../Apple_point".visible = false
			task = 2
			$"../../CanvasLayer/Quest_list/RichTextLabel".text = "Текущие квесты: \n"
			task_accept = true
			$"../../CanvasLayer/Quest_list/RichTextLabel".text += "Вернись к искателям приключений"
```

Все что осталось дополнить вход в зону

```gdscript
func _on_guild_of_heroes_body_entered(body):
	if body.name == "Player":
		$Label_quest.visible = true
		$Button.visible = true
		if task == 2:
			$Button.visible = false
			Quest.remove_task(task)
			$Label_quest.text = "Отлично! Мы подумаем над твоим запросом"
			$Label_quest.visible = true
```

Также создадим стены нашей деревни. Для этого создадим `tilemap` со следующими параметрами `tileset`

![image](https://github.com/Sindikaty/byteschool/assets/158248099/2c59d124-1003-4d29-9485-e6fd1ccf2168)

А также нужно включить автоматическую сортировку слоев у `tilemap`

![image](https://github.com/Sindikaty/byteschool/assets/158248099/74ef6760-a48b-435d-90fe-c0299212ff38)

Получится примерно следующее

![image](https://github.com/Sindikaty/byteschool/assets/158248099/74f1cd9b-fe2a-470f-905e-71f2a63d9265)

Также можно сделать таверну и попробовать добавить там квест на поиск предмета

Таверна состоит из следующий узлов

![image](https://github.com/Sindikaty/byteschool/assets/158248099/0fad591c-bd92-499d-b657-bb2c815a13d2)

Для входа создаем зону 

![image](https://github.com/Sindikaty/byteschool/assets/158248099/b3ca2b6b-f0b6-481d-8309-4d7ee6111308)

![image](https://github.com/Sindikaty/byteschool/assets/158248099/86d94132-3cf8-44f4-8622-bfc04daba635)

Скрипт бота

![image](https://github.com/Sindikaty/byteschool/assets/158248099/df573500-e046-4641-b97f-0c9ebf887ae9)

![image](https://github.com/Sindikaty/byteschool/assets/158248099/f79d3ba1-9b8c-44e3-a57b-45bf086310c3)

Скрипт NPC в таверне

```gdscript
var task = 0
var task_accept = false

func _on_quest_npc_body_entered(body):
	if body.name == "player":
		$QuestNPC/Label.visible = true
		$QuestNPC/Button.visible = true
		if GlobalScript.object_take == true:
			$QuestNPC/Button.visible = false
			GlobalScript.remove_task(task)
			$QuestNPC/Label.text = "Отлично! Мы подумаем над твоим запросом"
			$QuestNPC/Label.visible = true
			GlobalScript.object_take == false

func _on_quest_npc_body_exited(body):
	if body.name == "player":
		$QuestNPC/Label.visible = false
		$QuestNPC/Button.visible = false

func _on_button_pressed():
	task_accept = true
	$QuestNPC/Label.visible = false
	$QuestNPC/Button.visible = false
	#$"../../../CanvasLayer/QuestList/RichTextLabel".text = "Не Волшебное яблоко"
	GlobalScript.add_task(task)
	task = 1
	GlobalScript.quest_take = true

func _on_ex_body_entered(body):
	if body.name == "player":
		GlobalScript.OutSide = true
		get_tree().change_scene_to_file("res://node_2d.tscn")
```

Скрипт предмета который находится за пределами таверны ( у сцены деревни)

```gdscript
func _physics_process(delta):
	if GlobalScript.quest_take == true:
		$Buildings/Apple.visible = true
	else:
		$Buildings/Apple.visible = false
	if GlobalScript.OutSide == true:
		GlobalScript.OutSide = false
		$Buildings/player.global_position = Vector2(511,659)

func _on_taverna_body_entered(body):
	if body.name == "player":
		get_tree().change_scene_to_file("res://taverna.tscn")

func _on_apple_body_entered(body):
	if body.name == "player":
		GlobalScript.quest_take = false
		GlobalScript.object_take = true
```

У таверны добавяем физические слои, чтобы нельзя было проходить сквозь стены

Сделаем меню игры, для этого солздаем отдельную сцену и делаем ее для запуска первой

![image](https://github.com/Sindikaty/byteschool/assets/158248099/ce93da98-e596-4e04-a501-3297707d4c14)

Состоит из следующий элементов

![image](https://github.com/Sindikaty/byteschool/assets/158248099/97cfcfd0-1fa2-4588-9f2b-f8f2390e5ff4)

И выглядит примерно так

![image](https://github.com/Sindikaty/byteschool/assets/158248099/14496949-6822-48e2-a574-7312fd0ee278)

Создадим сундук с которого будут выпадать монеты для покупки питомцев. Состоит из следующих узлов

![image](https://github.com/Sindikaty/byteschool/assets/158248099/f1e4d9d8-7b4f-41ce-a163-3e031bd55521)

Создаем сцену с монеткой

![image](https://github.com/Sindikaty/byteschool/assets/158248099/027c17eb-c4a9-43f9-98a0-5c29342375b0)

Код сундука

```gdscript
extends Area2D

@export var coin_scene: PackedScene
@export var min_coins = 1
@export var max_coins = 5
var player_in_range = false
var use = false

func _on_body_entered(body):
	if body.name == "player":
		$Label.visible = true
		player_in_range = true
		$Label.text = "Нажмите Е чтобы открыть сундук"

func _process(delta):
	if player_in_range and Input.is_action_just_pressed("use1") and use == false:
		open_chest()
		use = true

func open_chest():
	var coin_count = randi() % (max_coins - min_coins + 1) + min_coins
	for i in range(coin_count):
		var coin_instance = coin_scene.instantiate()
		var chest_position = global_position
		var offset = Vector2(randf() * 64 - 32, randf() * 64 - 32)  # Случайное смещение вокруг сундука
		coin_instance.position = chest_position + offset
		get_parent().add_child(coin_instance)
	$Label.visible = false  # Скрыть метку после открытия сундука
	player_in_range = false  # Игрок больше не в зоне сундука
```

Код монетки

```gdscript
extends Area2D

func _on_body_entered(body):
	if body.name == "player":
		GlobalScript.Coins += 1
		$"../../CanvasLayer/QuestList/Label".text = "Количество монет - " + str(GlobalScript.Coins)
		queue_free()
```

И можно изменить торговца и добавить ему продажу петомцев за монетки

```gdscript
	if pet_count < 1 and GlobalScript.Coins >= 5:
		var pet = pet_snake.instantiate()
		pet_count += 1
		pet.position = $".".position
		get_parent().add_child(pet)
		$"../../CanvasLayer/Pet_tailor/RichTextLabel".text = "Отлинчый выбор!"
		GlobalScript.dialog = false
	elif pet_count > 1 and GlobalScript.Coins >= 5:
		$"../../CanvasLayer/Pet_tailor/RichTextLabel".text = "У тебя уже есть питомец"
		GlobalScript.dialog = false
	elif pet_count < 1 and GlobalScript.Coins <= 5:
		$"../../CanvasLayer/Pet_tailor/RichTextLabel".text = "У тебя не хватает денег, сходи заработай"
		GlobalScript.dialog = false
```

Пожилые анимации монеток

![image](https://github.com/Sindikaty/byteschool/assets/158248099/4355c992-c96b-40f7-b88b-e3325d12ed9e)

а

## Допы

### NPC-питомцы

Теперь неужно добавить самих питомцев которых будет продавать NPC. Для каждого питомца создаем отдельные сцены состаящие из следующих узлов

![image](https://github.com/Sindikaty/byteschool/assets/158248099/2050358a-7455-48a0-b58f-5dd04af9afc2)

Для создания передвижения питомца нам понадобится 2 переменные 

```gdscript
@export var speed = 100
var player_position
```

В методе `_ready` мы определяем позицию игрока, после чего в `_physics_process` мы также определяем позицию игрока и создаем локальную переменную которая определяет расстояние от питомца до игрока, после чего создаем проверку на это расстояние, если оно меньше 50 питомец двигается к нам. 

```gdscript
func _ready():
	player_position = $"../Player".position

func _physics_process(delta):
	player_position = $"../Player".position
	var distance = position.distance_to(player_position)
	 
	if distance > 50:
		var direction = (player_position - position).normalized()
		set_velocity(direction * speed)
		move_and_slide()

		if direction.x > 0 and speed > 0:
			$AnimatedSprite2D.play("walk")
			$AnimatedSprite2D.flip_h = false
		elif direction.x < 0 and speed > 0:
			$AnimatedSprite2D.play("walk")
			$AnimatedSprite2D.flip_h = true
	else:
		$AnimatedSprite2D.play("idle")
```

Все что нам осталось это добавить спавн питомцев при нажатии на кнопку. Для этого в основном уровне создаем 2 переменные в которые мы предварительно загружаем сцены.

```gdscript
var pet_wolf = preload("res://pet.tscn")
var pet_bear = preload("res://bear.tscn")
```

Присоединяем 2 сигнала на кнопки и создаем в них клон наших питомцев.

```gdscript
func _on_option_1_pressed():
		var pet = pet_wolf.instantiate()
		pet.position = $".".position
		get_parent().add_child(pet)
		$"../../CanvasLayer/torgovec_dialog/RichTextLabel2".text = "Отлинчый выбор! Он в цирке не выступает"

func _on_option_2_pressed():
		var pet = pet_bear.instantiate()
		pet.position = $".".position
		get_parent().add_child(pet)
		$"../../CanvasLayer/torgovec_dialog/RichTextLabel2".text = "Ну слушай... Зато к тебе и близко никто не подойдет"
```

Можно также добавить проверку на количество питомцев, для этого добавим переменную и проверку

```gdscript
pet_count = 0

func _on_option_1_pressed():
	if pet_count < 1:
		var pet = pet_wolf.instantiate()
		pet_count += 1
		pet.position = $".".position
		get_parent().add_child(pet)
		$"../../CanvasLayer/torgovec_dialog/RichTextLabel2".text = "Отлинчый выбор! Он в цирке не выступает"
	else:
		$"../../CanvasLayer/torgovec_dialog/RichTextLabel2".text = "У тебя уже есть питомец"
		
func _on_option_2_pressed():
	if pet_count < 1:
		var pet = pet_bear.instantiate()
		pet_count += 1
		pet.position = $".".position
		get_parent().add_child(pet)
		$"../../CanvasLayer/torgovec_dialog/RichTextLabel2".text = "Ну слушай... Зато к тебе и близко никто не подойдет"
	else:
		$"../../CanvasLayer/torgovec_dialog/RichTextLabel2".text = "У тебя уже есть питомец"
```
