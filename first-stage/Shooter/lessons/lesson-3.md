# Урок 3

## Краткое содержание
- Создание врагов
- Спавн врагов

## Создание врагов

Сегодня будем делать врагов

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/enemy_shooter.png">

Состоять враг будет из следующих узлов:

- `CharacterBody2D` - базовый узел для создания игрока и `NPC`, переименуйте его в `Enemy` или `Bot`
- `Sprite2D` - узел для спрайтов (так же подойдет `AnimatedSprite2D`, если у вас есть несколько анимаций)
- `CollisionShape2D` - узел для коллизий
- `NavigationAgent2D` - узел для навигации. Если есть навигационная карта, то объект сможет по ней перемещаться
- `Timer` - нужен будет для обновления маршрута до игрока

Загружаем необходимый спрайт(ы) и создаем коллизии. `Timer` пока оставляем, его настроим чуть позднее.

### Переходим к скрипту

Полный скрипт:
```gdscript
extends CharacterBody2D

const SPEED = 60
@onready var player = get_node("/root/Game/Player")
var hp = 20
@onready var nav_agent := $NavigationAgent2D as NavigationAgent2D


func _physics_process(_delta: float) -> void:
	var next_path_pos := nav_agent.get_next_path_position()
	var direction := global_position.direction_to(next_path_pos)
	velocity = direction * SPEED
	look_at(player.global_position)
	move_and_slide()


func makepath():
	nav_agent.target_position = player.global_position


func taking_damage():
	hp -= 10
	if hp <= 0:
		queue_free()
		const EXPLOSION_SCENE = preload("res://Scenes/VFX/explosion.tscn")
		var explosion = EXPLOSION_SCENE.instantiate()
		get_parent().add_child(explosion)
		explosion.global_position = global_position


func _on_timer_timeout():
	makepath()
```

Создавать функцию замедления мы будем у игрока, поэтому возвращаемся в его скрипт и создаем там еще 2 переменные.

```gdscript
@export var force : float = 0.2 # Переменная ответающая за то на сколько будет замедлятся игра
var slow_dash : bool = false # Переменная которая будет проверять включен ли слоумо
```

Перейдем к созданию самой функции

```gdscript
func slowmotion():
	if Input.is_action_just_pressed("slowmo"): # Проверяем, была ли нажата кнопка "slowmo"
		Global.slowmo = not Global.slowmo # Меняем значение переменной Global.slowmo на противоположное
		if Global.slowmo == true: # Если замедленное время включено
			Engine.time_scale = force # Устанавливаем значение движка на force, чтобы внутриигровые часы медленне тикали
    			slow_dash = true # Включаем переменную slow_dash
		else: # Если замедленное время выключено:
			Engine.time_scale = 1 # Возвращаем стандартное значение внутриигровым часам
			slow_dash = false # Выключаем переменную slow_dash
```

Теперь практически все будет замедляться при использовании слоумо, однако далеко не все, например, звуки и функция рывка не будет замедлена, из-за чего даже в слоумо все звуки и рывок будут как при обычной игре. Чтобы это исрпавить начнем с изменения функции `dash`
У нее мы добавим проверку на включенное замедление
```gdscript
func dash(delta):
	if slow_dash: # если время замедлено, то это условие
		transform.origin = lerp(transform.origin, transform.origin + 2 * input_vector , 0.5)
	else: # деш не в замедле 
		transform.origin = lerp(transform.origin, transform.origin + 40 * input_vector , 0.1)
```

А также добавим функцию `slowmo` в оружие для замедления проигрывания звука стрельбы

```gdscript
func slowmo():
	if Global.slowmo == true:
		$sound_gun.pitch_scale = 0.8
	else:
		$sound_gun.pitch_scale = 1
```

### Создание врагов

Для начала создадим CharacterBody2D и доабвим к нему следующие узлы:
* AnimatedSprite2D
* CollisionShape2D
* NavigationAgent2D
* Timer (включить автостарт)

Также нам нужно сздать Навигационный слой у TileMap, иначе враг не сможет понять где он сможет двигаться

Создание Навигационного слоя 

![image](https://github.com/Sindikaty/byteschool/assets/158248099/5231c31d-beee-41a9-a186-c481139c99b4) 

Выбор тайлов под Навигационный слой

![image](https://github.com/Sindikaty/byteschool/assets/158248099/f1faa4b9-6c17-4504-a4d6-4f7d8dfa56a9)

Перейдем к скрипту

Для начала сделаем следование ботов за игроком. Для этого нам понадобятся следующие переменные

```gdscript
const speed = 100
@export var player: Node2D
@onready var nav_agent := $NavigationAgent2D as NavigationAgent2D
@onready var playa = get_node("/root/level/player")
```

```gdscript
func _physics_process(_delta: float) -> void:
	var dir = to_local(nav_agent.get_next_path_position()).normalized() # Извлекаем направление движения к следующей точке пути и нормализуем его
	velocity = dir * speed # Устанавливаем скорость движения персонажа в направлении полученного вектора dir.
	if dir.x > 0: # Проверяем направление движения по оси X и изменяем ориентацию спрайта соответственно.
		$AnimatedSprite2D.flip_h = false
	else:
		$AnimatedSprite2D.flip_h = true
	if dir != Vector2(0,0): # Анимация проигрывается если враг движется
		$AnimatedSprite2D.play("walk")
```
Для составления пути создадим следующую функцию 

```gdscript
func makepath() -> void:
	nav_agent.target_position = playa.global_position
```
Теперь нужно сделать, чтобы она где-то вызывалась. Для этого мы создали Timer который каждую секунду будет вызывать данную функцию и строить путь
```gdscript
func _on_timer_timeout():
	makepath()
```

После того как мы сделали движение врагов, можно перейти к следующей не менее важной функции. Это функция получения урона врагами. Для этого создадим функцию dmg
```gdscript
func dmg():
	hp -= 10
	if hp <= 0:
		queue_free()
```
А также нужно добавить в скрипт пули вызов данной функции. Для этого добавим в условие еще одно, которое будет проверять имеет ли столкнувшийся объект метод "dmg" и если да, то вызывать его
```gdscript
func _physics_process(delta):
	global_position += movement_vector.rotated(rotation) * speed * delta
	var collide = move_and_collide(motion * delta)
	if collide:
		if collide.get_collider().has_method("dmg"): # Проверяем, имеет ли столкнувшийся объект метод "dmg" (нанесение урона).
			collide.get_collider().dmg() # Вызываем метод "dmg" у столкнувшегося объекта для нанесения урона.
		queue_free()
```
Все что осталось сделать так это добавить чтобы враги нас тоже могли убивать. Для этого создадим функцию take_damage_e() у `врагов` который будет при помощи цикла проверять наличие столкновений, и в случае если они происходят будет вызываться функция получения урона у игрока
```gdscript
func take_damage_e():
	for i in get_slide_collision_count():
		var obj = get_slide_collision(i).get_collider()
		if obj is CharacterBody2D and obj.name == "player":
			obj.take_damage_p()
```
Данную функцию и переменную нужно создать у игрока. Она будет вызыватся при столкновении со врагами
```gdscript
@export var hp = 100.0

func take_damage_p():
	hp -= 1
	if hp == 0:
		print('dead')
```
Теперь осталось сделать чтобы функция нанесения урона врагом где-то вызывалась. Мы добавим ее в `_physics_process` врага
```gdscript
func _physics_process(_delta: float) -> void:
	...
	take_damage_e()
```

Последнее что мы на сегоджня добавим это интересная анимация источников света вокруг игрока

Для нее создадим обычную 2d сцену и добавим следующие узлы:
* PointLight2D (х3)
* AnimationPlayer

Источники света расположим примерно так. Цвет источников можно задать любой

![image](https://github.com/Sindikaty/byteschool/assets/158248099/a8a4a5ae-537f-428a-985a-14d2c08a13d7)

И теперь создадим небольшую анимацию. В ней мы будем изменять свойство `rotation` у основного узла `Node2D`. Значение rotation у анимации 0, 180 и 360, а также стоит не забыть включить автостарт

![image](https://github.com/Sindikaty/byteschool/assets/158248099/620232dd-6b6f-400e-bfa7-5f52ac6afd85)

Остается добавить анимацию на уровень или прикрепить к игроку и получится примерно следующая анимация

![Godot Engine Nvidia Profile 2024 04 05 - 13 52 07 02_Trim (1)](https://github.com/Sindikaty/byteschool/assets/158248099/92cf7ab4-e288-41dc-a745-585cd8c91929)

Можно сделать переливающийся задний фон

Для него нам нужен ColorRect и AnimationPlayer в котором мы задаем смену цветов

![image](https://github.com/Sindikaty/byteschool/assets/158248099/9f020650-6b3a-442b-8ff6-06f958277f63)
