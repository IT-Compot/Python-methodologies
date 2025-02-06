## Урок 2

## Краткое содержание
- Создание пули
- Добавление бота

### Создание пули
![image](https://github.com/Sindikaty/byteschool/assets/158248099/5bc84a31-b1c2-4c68-83e0-34c0203ae5f9)

Базово для создания пушки потребуются следующие узлы:

* Sprite2D - Главный узел, является узлом для спрайтов
* Marker2D - Необходим для редактирования двухмерного пространства. Задать точку спавна, вылет пули и т.д.
* AudioStreamPlayer2D - Нужен для позиционированного звукогового сопровождения

Перейдем к скрипту

Для начала сделаем поворот пушки и ее отзеркаливание при достижении определенных градусов

>[!IMPORTANT]
> Градусы при которых пушка будут зеркалиться зависит от размера пушки (спрайта)

```gdscript
func _physics_process(delta):
	var mouse_pos = get_global_mouse_position() # переменная куда сохраняется глобальная позиция мыши
	look_at(mouse_pos) # метод который поворачивает текущий узел в сторону указанного объекта
	if global_rotation_degrees > 90 or global_rotation_degrees < -90: # условие при котором если глобальные градусы поворота спрайта превышают 90 или меньше -90
		self.flip_v = true # если условие выше является истиной, то спрайт зеркалится
	else: # иначе
		self.flip_v = false # не зеркалится
```

Теперь начнем делать выстрел, однако чтобы наша пушка могла стрелять нам нужны патроны. Для этого создадим новую сцену нашего патрона

Для создания патронов потребуются следующие узлы:

* RigidBody2D
* MeshInstance2D
* CollisionShape2D
* PointLight2D

![image](https://github.com/Sindikaty/byteschool/assets/158248099/2d1e7409-b03b-4b57-b917-ec805dec6a88)

Также можно добавить элемент VisibleOnScreenNotifier2D который позволять нам удалять те пули которые находят за экраном нашей игры
![image](https://github.com/Sindikaty/byteschool/assets/158248099/e2017057-33cd-45af-b1b7-d529715ed1e4)

Для этого у него присоединим узел screen_exited()

![image](https://github.com/Sindikaty/byteschool/assets/158248099/0945adb7-2c9a-4299-a913-9642f380af02)

И в скрипте пропишем
```gdscript
func _on_visible_on_screen_notifier_2d_screen_exited():
	queue_free()
```
А также добавим удаление патронов при касании с какими-либо физическими объектами
Для этого добавим у `RigidBody2D` переменную 
```gdscript
var motion = Vector2()
```
И пропишем следующий скрипт
```gdscript
func _physics_process(delta):
	var collide = move_and_collide(motion * delta)
	if collide:
		queue_free()
```
Теперь вернемся к нашей пушке и в ее коде создадим новую функцию которая будет отвечать за выстрел. 
Для нее нам понадобится 3 переменных 
```gdscript
var can_fire = true # проверка на возможность стрельбы
var bullet = preload("res://bullet.tscn") # подгрузка сцены с пулей
var bullet_speed = 1000 # скорость пули
```
И сама функция стрельбы
```gdscript
func shoot():
	if can_fire: # если игрок может стрелять
		var bullet_instance = bullet.instantiate() # инстанцируется пуля (создается экземпляр указанной сцены, клон проще говоря)
		$bullet_point.position = Vector2(23, -8) # позиция Marker2D (точка вылета пули) мы ставим в позицию которая находится примерно около рук персонажа
		bullet_instance.global_position = $bullet_point.global_position # глобальная позиция инстанцированной пули и точки вылета пули совпадают
		bullet_instance.apply_impulse(Vector2(bullet_speed, 0).rotated(get_parent().rotation), Vector2()) # задаем импульс для инстацнированной пули со скоростью пули и методом указываем направление родительского узла, а вторым вектором - ничего
		get_parent().get_parent().add_child(bullet_instance) # получаем родительский узел дважды и добавляем в сцену нового ребенка, который является инстанцированной пулей
		$sound_gun.play() # проигрывание звука пули
		can_fire = false # запрещаем стрелять игроку
		await get_tree().create_timer(0.5).timeout # Генератор таймера, который истечет за указанное время в скобках (проще говоря это у нас скорострельность пушки)
		can_fire = true # разрешаем пальбу
```
Все что нам осталось это добавить кнопку которая будет отвечать за стрельбу и прописать условия на ее нажатие
```gdscript
func _physics_process(delta):
...
	if Input.is_action_pressed("fire"):
		shoot()
```
### Создание тряски камеры

И последним что мы сделаем на этом уроке, это сделаем тряску камеры при стрельбе. Для нее нам понадобится глобальный скрипт.

Для его создания в меню скриптов нужно нажать `Файл` -> `Новый скрипт` и создать скрипт с названием global или каким-то подобным, после чего зайти в настройки проекта и добавить его в атозагрузку

![image](https://github.com/Sindikaty/byteschool/assets/158248099/69ce34c0-0918-4481-b92d-c2ed9d0ea30d)

```gdscript
var camera = null
```

Для создания тряски прикрепим скрипт к камеры, а также добавим ей `Timer`

![image](https://github.com/Sindikaty/byteschool/assets/158248099/9ad5bb03-c538-425d-875a-193f715db403)

Создадим 3 переменные которые нам понадобсятся для создания тряски экрана
```gdscript
var shake_amount : float = 0
@onready var timer : Timer = $Timer
@onready var tween : Tween = create_tween()
```

Устанавливаем процесс обновления, устанавливаем Global.camera в текущий узел и вызываем функцию randomize().

```gdscript
func _ready():
	set_process(true)
	Global.camera = self
	randomize()
```
Теперь генерируем случайное смещение для создания эффекта тряски.

```gdscript
func _process(_delta: float):
	offset = Vector2(randf_range(-3, 3) * shake_amount, randf_range(-3, 3) * shake_amount)
```
Теперь создадим функцию shake, которая запускает тряску камеры на заданное время с заданным количеством тряски.
```gdscript
func shake(time: float, amount: float):
	timer.wait_time = time
	shake_amount = amount
	set_process(true)
	timer.start()
```
Теперь присоединим узел `_on_timer_timeout()` таймеру. В нем мы останавливаем процесс обновления и запускаем анимацию плавного возвращения камеры в исходное положение.
```gdscript
func _on_timer_timeout() -> void:
	set_process(false)
	tween.interpolate_value(self, "offset", 1, 1, Tween.TRANS_LINEAR, Tween.EASE_IN)
```

Теперь все что нам осталось добавить вызов функции в функцию `shoot()` у оружия

```gdscript
Global.camera.shake(0.2, 1)
```
