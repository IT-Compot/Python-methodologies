## Урок 4

Для начала добавим количество патронов нашему игроку. Для этого зайдем в скрипт оружия и добавим переменные отвечающие за количество патронов

```gdscript
var ammoInMagazine = 30
var maxAmmoInMagazine = 30
```
А также немного изменим функцию стрельбы. Нам нужно добавить в условие проверку на количество патронов, а также добавить их убавление при выстреле
```gdscript
	if can_fire and ammoInMagazine > 0:
		...
		ammoInMagazine -= 1
		...
```

Теперь после 30 выстрелов у нас пропадет возможность стрельбы, поэтому следующим шагом мы добавим зоны поднятия оружия. Для нее нам понадобится:

* Area2D
* CollisionShape2D
* Sprite2D
* Timer
* Label

По итогу у нас получится что-то подобное

![image](https://github.com/Sindikaty/byteschool/assets/158248099/a1c4231d-5fcf-4f37-b114-4554fda4becf)

Перейдем к скрипту

Для начала добавим переменные. Первые 3 отвечают за наши дочерние узлы, а оставшиеся 2 являются логическими и буду нужны для проверок на поднятие патронов

```gdscript
@onready var timer = $Timer
@onready var collision_shape_2d = $CollisionShape2D
@onready var label = $Label
@onready var ammoPickedUp = false
var canPick : bool = true
```

Присоединим узел `_on_body_entered` к нашей зоне и начнем делать подбор оружия

```gdscript
func _on_body_entered(body):
	if body.name == "player" and canPick:
		collision_shape_2d.disabled = true # убираем коллизию 
		body.call("pickupAmmo") # вызываем метод pickupAmmo
		timer.start() # включаем таймер
		ammoPickedUp = true # патроны подняты = тру
		canPick = false # можем поднять еще = фолс
```

Как мы видим мы обращаемся к функции `pickupAmmo` которой у нас еще нет, поэтому переходим в скрипт игрока и создаем там эту функцию

```gdscript
@onready var stateGun = get_node("gun") # узел нашего оружия

func pickupAmmo():
	stateGun.ammoInMagazine = stateGun.maxAmmoInMagazine 
```

Теперь мы можем поднять оружие 1 раз, для того чтобы мы могли делаеть это несколько раз с какой-то периодичностью нам нужно присоединить узел к таймеру `_on_timer_timeout`
```gdscript
func _on_timer_timeout():
	collision_shape_2d.disabled = false # включем коллизию
	timer.stop() # выключаем таймер
	label.text = ""
	ammoPickedUp = false # патроны подняты = фолс
	canPick = true # можем поднять еще = тру
```

По сути поднятие оружие готово, но для удобства можно добавить `label` в котором будет выводится время когда можно будет поднять оружие в следующий раз
```gdscript
func _process(delta):
	if ammoPickedUp:
		label.text = str(int(timer.time_left))
```

Респавн ботов

Для создания спавнера ботов на нужны следующие элементы:
* Marker2D
* Timer (автостарт)
  
Создавать мы их будет на нашем уровне

Перейдем к скрипту

```gdscript
@export var spawn_scene : PackedScene  # Экспортируем переменную spawn_scene типа PackedScene
```

Тип PackedScene в Godot Engine представляет собой упакованную сцену, которая содержит информацию о ресурсах и узлах сцены. Он используется для загрузки и создания экземпляров объектов сцены во время выполнения программы. Когда вы загружаете сцену в редакторе Godot, она сохраняется в формате .tscn, который затем может быть упакован в один файл .pck с помощью инструмента упаковки ресурсов.
Создаем функцию спавна

```gdscript
func spawn(_spawn_scene := spawn_scene) -> void:  # Определяем функцию spawn с параметром _spawn_scene по умолчанию spawn_scene
  var spawn := _spawn_scene.instantiate() as Node2D  # Создаем экземпляр объекта из PackedScene и приводим его к типу Node2D
  add_child(spawn)  # Добавляем созданный объект в качестве дочернего

  spawn.global_position = global_position  # Устанавливаем глобальную позицию созданного объекта равной глобальной позиции текущего объекта
```

Вызываем функцию создания объекта в сигнале `timeout()` у таймера

```gdscript	
func _on_timer_timeout():  # Обработчик события таймера
  spawn()  # Вызываем функцию spawn для создания объекта
```
А также нужно не забыть выбрать сцену спавна. В нашем случае это сцена с врагом

![image](https://github.com/Sindikaty/byteschool/assets/158248099/b74c47ce-fb49-4d34-aaa5-bf68bcc1c358)

Все основные механики готовы, осталось лишь сделать UI

Начнем с добавления ProgressBar нашим слаймам

![image](https://github.com/Sindikaty/byteschool/assets/158248099/7dc28a6d-89a3-4fa4-abd3-71ec45b62550)


![image](https://github.com/Sindikaty/byteschool/assets/158248099/37299c3c-09f9-4640-8183-f7a1da71556e)

И прописываем следующее в скрипте

```gdscript
func _physics_process(_delta: float) -> void:
	...
	$hp_bar.value = self.hp
	...
```

Следующим элементом можно добавить интерфейс для игрока (его хп, патроны и можно добавить фпс). Для этого создаем новой сценой CanvasLayer

Начнем с отображения патронов. Добавляем Sprite2D и Label после чего располагаем их в пределах видимости CanvasLayer, например, так

![image](https://github.com/Sindikaty/byteschool/assets/158248099/960d1de6-607f-4544-8f31-47e108a62bbd)

И прописываем следующее в скрипте Нашего Канваса

```gdscript
func _process(delta):
	$AssaultRifle/Label.text = str($"..".stateGun.ammoInMagazine)
```

Следующим добавим отображение хп игрока. Для этого добавим ProgressBar в CanvasLayer и прописываем следующее в скрипте игрока

```gdscript
func _physics_process(delta: float):
	...
	$ui_fps2/UI/ProgressBar.value = hp
 	...
```

Также можно добавить отображение фпс. Для него мы добавим Label и к нему прикрепим скрипт
```gdscript
@export var enabled := true

func _process(delta: float) -> void:
	if enabled:
		var frames : float = Engine.get_frames_per_second()
		text = "FPS: "
		text += str(frames)
```

Можно также добавить музыку на уровне. Для этого добавляем `AudioStreamPlayer2D` на наш уровень, а также не забываем о том, что у нас есть слоумо и в скрипте уровня нужно будет замедлять его если мы в слоумо

```gdscript
func _process(delta):	
	if Global.slowmo == true:
		$"Music_background".pitch_scale = 0.8
	else:
		$"Music_background".pitch_scale = 1
```

Осталосб добавить чтобы при смерти все процессы останавливались и была возможность рестарта
