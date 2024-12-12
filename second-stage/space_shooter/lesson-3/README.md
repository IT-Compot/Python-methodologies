# КосмоШутер | Урок 3

Занятие посвящено продвинутому перемещению 3D-объекта (в нашем случае космический корабль).

## Содержание

(содержание)

## План на занятие 

Сегодня напишем (что напишем)\
Познакомимся с новыми понятиями ()\
\
Начнём!

### Что ещё необходимо кораблю

Для полноценного управления мы хотим поворачивать вправо-влево. Но так как мы находимся в космосе, мы можем также двигаться вверх-вниз.\
По-английски:\

1) движение носа корбля влево-вправо будет звучать как `yaw`, по-русски *рыскание*.
2) движение носа корбля вверх-вниз будет звучать как `pitch`, по-русски *тангаж*.
3) вращение вокруг совей оси будет звучать как `roll`, по-русски *вращение*.

Создадим необходимые переменные скорости для всех этих явлений:

```GDScript
@export var yaw_speed = 1.5
@export var pitch_speed = 1.5
@export var roll_speed = 3.0

var current_yaw : float = 0.0
var current_pitch : float = 0.0
var current_roll : float = 0.0

@export var input_response = 8.0
```

Мы добавили также экспортную переменную input_response, которая нужна нам для указания скорости отзывчивости корабля на нажатия клавиш.\
Готово, после создания переменных идём модифицировать код.\

### Пишем скрипт

Перейдём в функцию get_input() и модифицируем её. Раньше мы писали условие для нажатия на одну клавишу, но сейчас перед нами более сложная задача, клавиш 6 и они представляют собой 3 пары противоположных направлений. Используем новую для нас функцию get_axis(), в аргументах которой можно записать сразу 2 клавиши, которые вернут нам значения 1 или -1.

![image](https://github.com/user-attachments/assets/04a41573-ba39-429f-88ec-000e9925c61e)

То же самое мы можем написать и для других клавиш:

![image](https://github.com/user-attachments/assets/17d81a6b-18af-40d0-b39c-0cbbfecf9bc7)

Функция get_input() готова:

```GDScript
func get_input(delta):
	if Input.is_action_pressed("increase_speed"):
		current_speed = lerp(current_speed, max_speed, acceleration * delta)
	if Input.is_action_pressed("reduce_speed"):
		current_speed = lerp(current_speed, max_negative_speed, acceleration * delta)
	if Input.is_action_pressed("reset"):
		current_speed = lerp(current_speed, 0.0, acceleration * delta)
		
	current_yaw = lerp(current_yaw, Input.get_axis("ui_right", "ui_left"), input_response * delta)
	current_pitch = lerp(current_pitch, Input.get_axis("ui_down", "ui_up"), input_response * delta)
	current_roll = lerp(current_roll, Input.get_axis("roll_right", "roll_left"), input_response * delta)
```

Теперь осталось только применить заданные значения `current_yaw`, `current_pitch` и `current_roll` в функции _physics_process(delta). Переходим в неё:

![image](https://github.com/user-attachments/assets/d82721cc-ae15-4b4a-9b84-aae7c034269d)

Меняем `transform.basis`, применяем к нему метод rotated(), в аргументах видим подсказки, что он принимает как первый аргумент вектор 3D, который мы будем менять, а как второй - угол, на который поворачиваем. Зададим эти параметры:

![image](https://github.com/user-attachments/assets/7127623c-4fd9-4331-a49d-71bb4af88c1b)

Напишем то же самое и для остальных осей:

![image](https://github.com/user-attachments/assets/dd3af4e5-fd3a-4544-a532-d8a887f0936a)

Итоговый код функции _physics_process(delta) получился следующим:

```GDScript
func _physics_process(delta: float) -> void:
	get_input(delta)
	
	transform.basis = transform.basis.rotated(transform.basis.y, current_yaw * yaw_speed * delta)
	transform.basis = transform.basis.rotated(transform.basis.x, current_pitch * pitch_speed * delta)
	transform.basis = transform.basis.rotated(transform.basis.z, current_roll * roll_speed * delta)
	
	velocity = -transform.basis.z * current_speed
	move_and_collide(velocity * delta)
```



