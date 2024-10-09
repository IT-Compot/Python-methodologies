## Урок 2

### Обычный бот

На этом уроке мы создадим самого обычного NPC (Non-player character) не дающего заданий. Основным узлом будет `CharacterBody2D` и к нему мы присоединяем `AnimatedSprite2D` и `CollisionShape2D`. Анимации и коллизию делаем как у игрока полсе чего переходим к скрипту.
А так же создаим бота, который будет выдавать задания игроку

![image](https://github.com/user-attachments/assets/1db6af3f-d422-4a10-9051-468f05dc4254)

> Как можно заметить - у ботов похожий спрайт, следовательно, то же самое смещение

Для реализации нам понадобятится 4 переменные

```gdscript
var move_dir = Vector2.ZERO
var move_speed = 50
var time_to_change_dir = 2
var timer = 0
```

После чего в process прописываем случайное перемещение бота каждые 2 секунды

```gdscript
func _process(delta):
	timer += delta;
	if timer >= time_to_change_dir:
		timer = 0
		move_dir = Vector2(randf_range(-1, 1), randf_range(-1, 1)).normalized()

	if move_dir == Vector2(0,0):
		$AnimatedSprite2D.play("idle")
	else:
		move_anim()
	
	set_velocity(move_dir * move_speed)
	move_and_slide()

func move_anim():
	if move_dir.x > 0:
		$AnimatedSprite2D.flip_h = false
	else:
		$AnimatedSprite2D.flip_h = true
		
	if move_dir.y > 0:
		$AnimatedSprite2D.play("walk_dwn")
	else:
		$AnimatedSprite2D.play("walk_up")
```

На уровне добавляем отдельный узел Node2D где будут хранится все NPC, после чего присоединяем туда наших ботов.
![image](https://github.com/user-attachments/assets/b1cc1e49-c488-454a-b1ab-fa5dad5720dc)

> Как видно, `Ordering`, а точнее свойство `Y Sort Enabled` - включен. Поэтому будет работать сортировка по Y у всех дочерних элементов 

## Квестодатель

Следующий подраздел начнем с создания персонажа у которого мы можем получить квест. К NPC добавим его анимацию, например так:

![QuestGiver gif](https://github.com/user-attachments/assets/0e3b5a80-82e0-444d-a7d9-ff07f405b89a)


>[!NOTE]
>Дети уже к концу курса должны быть на опыте, поэтому можно спокойно отдать часть с настройкой анимации на самостоятельную реализацию.
>Коллизии лучше сделать с ними, так как их настройка будет зависеть от расположения этого персонажа

Используем мы `CollisionPolygon2D` потому что через него можно задать необходимую область для персонажа, но если ребенок совсем Easy, то можно сделать `CollisionShape2D`. 

Как работать с `CollisionPolygon2D`:

![MakingCollisions](https://github.com/user-attachments/assets/b51c6994-d4ee-496f-8559-24d0f95d6bd2)



Теперь нам нужно создать сам диалог с продавцом, для этого создадим `CanvasLayer` и в нем узел `Control`.
![image](https://github.com/user-attachments/assets/52e9814e-2976-426c-b8b7-25bdf666cafd)


>[!TIP]
>Для удобства привыкайте переименовывать узлы, чтобы было понятнее и проще работать с ними в будущем.


Также нам понадобятся следующие элементы:
* `Panel` 2x (рамка диалогового окна и рамка текста)
* `Label` 2x (Имя персонажа и текст самого NPC)
* `Button` 2x (Выбор ответа)
* `AnimatedSprite2D` (Персонаж)

И приходим примерно к этому:

![image](https://github.com/user-attachments/assets/b9fecb72-ae51-4c65-9983-7075cda0e6fc)

>[!NOTE]
>Конечно вы можете сделать свой вариант. И дети тоже могут. Проявите свою творческую сторону!

![image](https://github.com/user-attachments/assets/9dd459dc-46e4-46aa-a5bc-bc11aec4a866)

>Такой вариант может быть даже лучше, сэкономит место, но вы в любом случае можете выбрать сами.

![image](https://github.com/user-attachments/assets/ba16a092-dcf6-4ecd-90a4-0662664cd4f9)


![image](https://github.com/Sindikaty/byteschool/assets/158248099/13fbe0d8-4b58-4a79-8d17-bc9ee9f960a9)

Прикрепляем скрипт и присоединяем сигналы на вход и выход из зоны персонажа и в них прописываем включение/выключение диалога соответственно

```gdscript
var in_area = false # эта переменная будет проверять в области ли игрок

func _process(delta):
	if in_area == true: # здесь проверяется в области ли игрок
		%QuestGiverWindow2.visible = true # обращение по уникальному имени узла
	else:
		%QuestGiverWindow2.visible = false


func _on_body_entered(body):
	if body.name == "Player": # проверка на имя узла, проверяйте имя узла игрока! Не сцены!
		in_area = true # если выражение выше является истинным, то тогда включаем эту переменную
		


func _on_body_exited(body):
	if body.name == "Player": # всё та же проверка
		in_area = false # здесь всё наоборот
```

>[!WARNING]
>Ты должно быть заметил, что в скрипте используется не <kbd>$</kbd> при обращении к узлу, а <kbd>%</kbd>. Сделано это для доступа к узлу по уникальному имени, т.е. можно обращаться к узлу, независимо от пути к этому узлу.

Делается это следующим образом:

![UniqueName](https://github.com/user-attachments/assets/29c851a7-7850-40cb-ba49-2ef9b44464f3)



Можно добавить проверку на диалог, чтобы маршрут не строился в случае диалога. Для этого создаем глобальный скрипт и добавляем изменение в зависимости от ситуации.

Если мы зашли в зону диалога делаем переменную true

```gdscript
func _on_area_2d_body_entered(body):
	if body.name == "player":
		in_area = true
		if in_area == true:
			GlobalScript.dialog = true
			$"../../CanvasLayer/Pet_tailor".visible = true
```

А если мы нажали по выбору питомца или он уже у нас есть мы делаем ее false

```gdscript
func _on_wolf_2_pressed():
	if pet_count < 1:
		var pet = pet_bear.instantiate()
		pet_count += 1
		pet.position = $".".position
		get_parent().add_child(pet)
		$"../../CanvasLayer/Pet_tailor/RichTextLabel".text = "Ну слушай... Зато к тебе и близко никто не подойдет"
		GlobalScript.dialog = false
	else:
		$"../../CanvasLayer/Pet_tailor/RichTextLabel".text = "У тебя уже есть питомец"
		GlobalScript.dialog = false
```

Следующего NPC которого мы сделаем будет стражник который рассказывает что где находится. Нам понадобятся следующие узлы:
* `Area2D`
* `AnimatedSprite2D`
* `CollisionShape2D`
* `Label`

MPC будет выглядить примерно так

![image](https://github.com/Sindikaty/byteschool/assets/158248099/c207a3d5-15f4-4dde-8834-0ef7d2b5b3c3)

Теперь нам нужно сздать сам диалог со стражником. Делать это мы будем в ранее созданном `CanvasLayer`. Основным узлом бьудет `Control` и к нему присоединяем следующие узлы:
* `Panel` х2
* `RichTextLabel`
* `Button` x4

Расставляем все и создаем скрипт у Control после чего присоединяем сигналы к кнопкам.

![image](https://github.com/Sindikaty/byteschool/assets/158248099/d27b2410-92b7-4c29-bbec-002ef9d1d688)

```gdscript
var variation_fact = 0


func _on_answer1_pressed():
	$RichTextLabel.text = "Просто иди дальше по дороге. Не ошибешься. Они полказны угрохали на этот замок."


func _on_answer2_pressed():
	$RichTextLabel.text = "Парень, она слева от тебя."


func _on_answer3_pressed():
	randomize()
	variation_fact = int(randf_range(0, 10))
	if variation_fact == 0:
		$RichTextLabel.text = "Что-то интересное? Я тебе что, библиотекарь что ли?"
	if variation_fact == 1:
		$RichTextLabel.text = "Говорят в городе завелся некий Давахин... Ничего не слышал об этом?"
	if variation_fact == 2:
		$RichTextLabel.text = "Хочешь что-то интересное - дуй в таверну. Там наслушаешься"
	if variation_fact == 3:
		$RichTextLabel.text = "Ты никому не говори, но я на самом деле хотел быть в разведотряде."
	if variation_fact == 4:
		$RichTextLabel.text = "А что если я тоже избранный? Я вон, в детстве в чан с облепиховым морсом упал."
	if variation_fact == 5:
		$RichTextLabel.text = "Если ты слышал местные слухи о слуге, который убил своего хозяина и стал стражником, то это не я"

func _on_answer4_pressed():
	$RichTextLabel.text = "Ага. Всего хорошего."
```

Теперь нужно добавить собственно появление этого диалога. Для этого создаем скрипт у Area2D нашего NPC

```gdscript
func _on_guard_body_entered(body):
	if body.name == "Player":
		$Label.visible = true
		$Label.text = "Чего тебе, приключенец?"
		$"../../CanvasLayer/dialog".visible = true
		
	if body.is_in_group("NPC"):
		$Label.visible = true
		$Label.text = "Не мешайте службе, житель"

func _on_guard_body_exited(body):
	if body.name == "Player":
		$Label.visible = false
		$"../../CanvasLayer/dialog".visible = false
		
	if body.is_in_group("NPC"):
		$Label.visible = false
```
