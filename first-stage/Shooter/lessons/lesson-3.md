# Урок 3

## Краткое содержание
- Создание врагов
- Спавн врагов

## Создание врагов

Сегодня будем делать врагов

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/enemy_shooter.png">

Создаем новую сцену.

Состоять враг будет из следующих узлов:

- `CharacterBody2D` - базовый узел для создания игрока и `NPC`, переименуйте его в `Enemy` или `Bot`. Крепим к нему скрипт
- `Sprite2D` - узел для спрайтов (так же подойдет `AnimatedSprite2D`, если у вас есть несколько анимаций)
- `CollisionShape2D` - узел для коллизий
- `NavigationAgent2D` - узел для навигации. Если есть навигационная карта, то объект сможет по ней перемещаться
- `Timer` - нужен будет для обновления маршрута до игрока

Загружаем необходимый спрайт(ы) и создаем коллизии. Для узла `Timer` включаем автостарт и ставим время примерно в 0.2 секунды. Так же присоединяем сигнал `timeout` к скрипту корневого узла и пока оставляем, как есть.


### Переходим к скрипту

Полный скрипт для быстрого ознакомления:
```gdscript
extends CharacterBody2D  

const SPEED = 60  # Скорость передвижения объекта (60 пикселей в секунду)

@onready var player = get_node("/root/Game/Player")  # Получаем ссылку на игрока (ищем в корне сцены)
var hp = 20  # Переменная для хранения очков здоровья

@onready var nav_agent := $NavigationAgent2D as NavigationAgent2D  
# Получаем ссылку на NavigationAgent2D, который помогает с прокладыванием пути


func _physics_process(_delta: float) -> void:
    var next_path_pos := nav_agent.get_next_path_position()  
    # Получаем следующую точку пути от агента навигации
    
    var direction := global_position.direction_to(next_path_pos)  
    # Определяем направление к следующей точке пути
    
    velocity = direction * SPEED  
    # Устанавливаем скорость движения в направлении точки
    
    look_at(player.global_position)  
    # Поворачиваем объект лицом к игроку
    
    move_and_slide()  
    # Двигаем объект, учитывая столкновения


func makepath():
    """Обновляет путь к игроку"""
    
    nav_agent.target_position = player.global_position  
    # Устанавливаем новую цель навигации — позицию игрока


func taking_damage():
    """Обрабатывает получение урона"""
    
    hp -= 10  # Уменьшаем здоровье на 10
    
    if hp <= 0:  
        # Если здоровье <= 0, удаляем объект и создаем взрыв
        
        queue_free()  # Удаляем текущий объект из сцены
        
        const EXPLOSION_SCENE = preload("res://Scenes/VFX/explosion.tscn")  
        # Загружаем сцену взрыва (preload загружает сцену заранее, в отличие от load)
        
        var explosion = EXPLOSION_SCENE.instantiate()  
        # Создаём экземпляр сцены взрыва
        
        get_parent().add_child(explosion)  
        # Добавляем взрыв в родительский узел
        
        explosion.global_position = global_position  
        # Устанавливаем взрыв в позицию текущего объекта


func _on_timer_timeout():
    """Вызывается, когда срабатывает таймер"""
    
    makepath()  # Обновляем путь к игроку

```

Теперь по порядку: создаем переменные для удобства.

```gdscript
@onready var player = get_node("/root/Game/Player") # укажите имя узла игрока
@onready var nav_agent := $NavigationAgent2D as NavigationAgent2D # можете создать такую переменную, чтобы было проще писать код

const SPEED = 60 

```

>[!Tip]
>Вы можете быстро создавать переменные, если удерживать кнопку <kbd>CTRL</kbd>, затем навестить курсором на узел, нажать на <kbd>Левую кнопку мыши</kbd> и перетащить таким образом в скрипт. Так вы быстро создадите переменную.

>[!Tip]
>Можешь рассказать для чего нужен `@onready`.<br>
>- `@onready` откладывает инициализацию переменной, пока сцена не будет загружена.<br>
>- Позволяет безопасно обращаться к нодам, которые уже есть в сцене.<br>
>- Улучшает производительность и читаемость кода.<br>

Примерное объяснение детям:
>Представь, что ты готовишь завтрак.
>Обычно, если ты пытаешься налить молоко в чашку, а молока ещё нет в холодильнике, то ничего не получится!
>
>Вот так же работает код без @onready – он пытается взять что-то до того, как оно появилось.
>
>А @onready – это как правило "Сначала открой холодильник, потом бери молоко".
>То есть ждём, пока всё будет готово, и только потом используем.
>
>В коде это означает:<br>
>🔹 Без @onready – пытаемся взять ноду слишком рано, и код может сломаться.<br>
>🔹 С @onready – ждём, пока сцена загрузится, и потом берём ноду.
>


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
