# КосмоШутер | Урок 2

Занятие посвящено базовому движению 3D-объекта (в нашем случае космический корабль).

## Содержание

(содержание)

## План на занятие 

Сегодня напишем плавное движение корабля вперёд-назад, познакомимся с новой функцией `lerp()`, увидим как работают экпортные переменные `@export` и чем они отличаются от обычных, добавим кнопки.\
\
Начнём!

### Создание скрипта

Теперь мы хотим управлять кораблём, значит прикрепим к нему скрипт. Прикрепляем его обязательно к самому кораблю на его личной сцене.

![image](https://github.com/user-attachments/assets/7fc8ab0d-5b58-4543-95d3-d12606dcd973)

Шаблон нам не понадобится, так как он описывает движение персонажа в игре типа "платформер", поэтому галочку с шаблона можно снять:

![image](https://github.com/user-attachments/assets/d6ca4ca5-9428-445c-8bce-731803f7fc96)

Создали пустой скрипт и давайте подумаем насчёт физики. В космосе мы можем лететь вперёд по прямой набирая положительную скорость, а если мы тормозим, то скорость уменьшается, значит она постепенно будет переходить в отрицательную. Создадим в скрипте два типа скорости и ускорение:

```GDScript
extends CharacterBody3D

@export var max_speed = 50.0
@export var max_negative_speed = -30.0
@export var acceleration = 0.6

var current_speed = 0.0
```
Ещё нам понадобится НЕ экспортная переменная текущей скорости current_speed, в которую мы будем записывать текущее значение скорости. По умолчанию она будет нулевой, но мы обязательно поставим точку, чтобы указать, что тип данных этой переменной - `float`, то есть число с плавающей точкой или не целое число.

Теперь мы можем создать клавиши для движения корабля, зайдём в `Проект` -> `Настройки проекта` и привяжем кнопки:

![21](https://github.com/user-attachments/assets/cd4f8301-f6f4-48f4-9fb5-2c873a15aae4)

Отлично, теперь возвращаемся к написанию скрипта. Создадим функцию get_input(), которая будет отвечать за нажатия на кнопки:

```GDScript
func get_input(delta):
	if Input.is_action_pressed("increase_speed"):
		pass
	if Input.is_action_pressed("reduce_speed"):
		pass
	if Input.is_action_pressed("reset"):
		pass
```

Пока что напишем в условиях `pass`, чтобы поочерёдно наполнять их логикой. В эту функцию мы передали `delta`, так как delta - это время между кадрами и оно нам понадобится для более плавного перемещения.

Теперь подумаем, что будет меняться при нажатии на все эти клавиши? Правильный ответ - текущая скорость, у нас для неё создана отдельная переменная. Чтобы текущая скорость у нас менялась плавно с течением времени и чтобы не было резких скачков корабля в пространстве, приравняем текущую скорость к результату отработки функции lerp(). `lerp()` - это линейная интерполяция, которая принимает три аргумента для её работы: 

1) текущую скорость,
2) скорость, к которой стремимся (максимальная), и
3) вес скорости (шагами какого размера будем приближаться к максимальной скорости).

Посмотрим как это выглядит в скрипте:

![image](https://github.com/user-attachments/assets/569d8f09-6e64-48d1-8779-f9b700a400b6)

Передадим все аргументы в эту функцию при том, что за вес скорости мы специально создали переменную acceleration (англ. ускорение), можно сразу расписать то же  самое и для кнопки `reduce_speed` - уменьшение скорости:

```GDScript
func get_input(delta):
	if Input.is_action_pressed("increase_speed"):
		current_speed = lerp(current_speed, max_speed, acceleration * delta)
	if Input.is_action_pressed("reduce_speed"):
		current_speed = lerp(current_speed, max_negative_speed, acceleration * delta)
	if Input.is_action_pressed("reset"):
		pass
```
Что ж, теперь мы хотим увидеть результат отработки функции get_input(), но как нам это сделать? Функцию нужно вызвать внутри другой функции, заранее описанной разработчиками движка. Это у нас будет `_physics_process(delta)`, она как раз по умолчанию получает delta, её мы и передадим в get_input():

```GDScript
func _physics_process(delta: float) -> void:
	get_input(delta)
```
get_input() отработает и изменит значение в переменной current_speed, то есть там будет лежать разное значение в зависимости от того, как мы понажимали на кнопки. Но корабль ещё не двигается, хотя скорость задана. Чего нам не хватает сделать? Конечно, передать эту скорость в функцию, которая будет перемещать объект и указать ось, по которой мы перемещаем. Это и сделаем с следующей строке:

![image](https://github.com/user-attachments/assets/cb94331f-1bf6-4f62-b821-eef2cac06309)

А далее передадим скорость в `move_and_collide()` и домножим её на delta. Получается следующий скрипт:

```GDScript
func _physics_process(delta: float) -> void:
	get_input(delta)
	velocity = -transform.basis.z * current_speed
	move_and_collide(velocity * delta)
```
`transform` домножили на -1 (стоит знак минус, то есть параметр отрицательный) потому что мы ранее развернули корабль в минусы по оси `Z`, поэтому летим вперёд в минусы.

Если вылетела ошибка следующего толка: ![image](https://github.com/user-attachments/assets/b6bb1e47-ba61-4282-af73-536a3d1b53a0), значит, где-то в скрипте мы пытаемся передать int'ы заместо float'ов. Найдем их, поставим .0 в конце, чтобы указать тип данных, и проблема решена.

Вот конечный вариант скрипта, написанного на данном этапе:

```GDScript
extends CharacterBody3D

@export var max_speed = 50.0
@export var max_negative_speed = -30.0
@export var acceleration = 0.6

var current_speed = 0.0

func get_input(delta):
	if Input.is_action_pressed("increase_speed"):
		current_speed = lerp(current_speed, max_speed, acceleration * delta)
	if Input.is_action_pressed("reduce_speed"):
		current_speed = lerp(current_speed, max_negative_speed, acceleration * delta)
	if Input.is_action_pressed("reset"):
		pass
		
		
func _physics_process(delta: float) -> void:
	get_input(delta)
	velocity = -transform.basis.z * current_speed
	move_and_collide(velocity * delta)
```



