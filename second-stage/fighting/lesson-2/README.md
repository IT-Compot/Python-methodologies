# Файтинг | Урок 2

(описание)

## Содержание

- [План на занятие](#План-на-занятие)
  - [Скрипт персонажа](#Скрипт-персонажа)
    - [Анимация ходьбы персонажа](#Анимация-ходьбы-персонажа)
    - [Анимация атаки персонажа](#Анимация-атаки-персонажа)
  - [Бот](#Бот)
    - [Горячие клавиши для работы со сценой](#Горячие-клавиши-для-работы-со-сценой)


## План на занятие 

(план на занятие)

### Скрипт персонажа

Прикрепляем скрипт персонажа на его сцене, можно взять шаблон для платформера:

![5](https://github.com/user-attachments/assets/b03e830f-76b5-4dd9-b5b8-8cf12655f2f3)

Оттуда мы уберём всё лишнее, связанное с прыжком и по итогу наш скрипт будет выглядеть вот так:

![image](https://github.com/user-attachments/assets/660aeaa6-7bf0-4b24-9e22-5a4ff6b67db0)

Или, если угодно, для копипасты, вот:

```GDScript
extends CharacterBody3D

const SPEED = 5.0

func _physics_process(delta: float) -> void:

	if not is_on_floor():
		velocity += get_gravity() * delta

	move_and_slide()
```
Создадим метод для старта анимации при запуске игры. Это будет метод, заранее существующий в движке, можно вспомнить как он называется:

```GDScript
func _ready() -> void:
	$AnimationPlayer.play("idle")
```

Помимо запуска анимации мы хотим нажимать на кнопки и видеть как в результате персонаж перемещается вправо-влево.\
Напишем для этого отдельный метод, на этот раз это будет созданный нами метод `move()`:

```GDScript
func move():
	if Input.is_action_pressed("ui_right"):
		velocity.z = -SPEED
	elif Input.is_action_pressed("ui_left"):
		velocity.z = SPEED
	else:
		velocity.z = 0
```

Не забудем вызвать его в функции `_physics_process(delta)`!\
Как мы видим, скрипт по своей структуре абсолютно идентичен управлению вправо-влево в платформере.\
\
Отлично, теперь займёмся анимациями.

### Анимация ходьбы персонажа

Для начала создадим переменную, куда запишем состояние анимации персонажа на данный момент:

```GDScript
var action = 'none'
```

В текстовом виде укажем, что действие персонажа равно ничему, то есть `none`.\
А теперь объявим метод, который будет запускать анимации в зависимости от того, чему равна эта переменная:

```GDScript
func animation():
	match action:
		"punch":
			$AnimationPlayer.play("punch")
		"leg_punch":
			$AnimationPlayer.play("leg_punch")
		"recieve_damage":
			$AnimationPlayer.play("recieve_damage")
		"forward":
			$AnimationPlayer.play("forward")
		"backward":
			$AnimationPlayer.play("backward")
		"none":
			$AnimationPlayer.play("idle")
		"dying":
			$AnimationPlayer.play("dying")
```
Не забудем вызвать новый метод `animation()` внутри функции `_physics_process(delta)`!\
\
Что ж, методы объявлены, теперь нужно изменять переменную `action`, чтобы всё работало и чтобы мы видели анимации.\
Начнём с простого движения, будем менять значение `action` когда мы нажимаем на кнопки:

![image](https://github.com/user-attachments/assets/f945cb7d-5919-465b-b439-1872d47f7bf7)

Теперь перед нами стоит новая проблема: персонаж не перестаёт проигрывать ходьбу когда мы остановились.\
Чтобы это исправить, прикрепим сигнал от узла `$AnimationPlayer`, который называется `_on_animation_finished(anim_name)`:

![6](https://github.com/user-attachments/assets/f2c28707-169f-4b11-bd1a-788ea0f6c00d)

Напишем внутри появившегося метода следующие условия:

```GDScript
func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	if anim_name == "punch":
		action = "none"
	elif anim_name == "leg_punch":
		action = "none"
	elif anim_name == "recieve_damage":
		action = "none"
	elif anim_name == "forward":
		action = "none"
```
Теперь можно запустить игру и посмотреть на результат. Персонаж ходит и анимация ходьбы прекращается как только мы отожмём кнопку.

### Анимация атаки персонажа

Чтобы персонаж атаковал ему нужны соответствующие кнопки. Созадим их в настройках проекта:

![6](https://github.com/user-attachments/assets/d01badb7-1a1e-409e-bf16-36ea1310a02a)

А теперь напишем скрипт, чтобы задействовать эти кнопки:

![image](https://github.com/user-attachments/assets/d88e47f0-db5b-4f92-8364-c55dbc269d80)

Теперь персонаж умеет атаковать.

### Бот

Настало время добавить в игру противника. Бот создаётся абсолютно аналогично, можно скачать анимации на сайте `mixamo`, не забудем создать для бота отдельную папку, чтобы не наводить беспорядок в файлах:

![20](https://github.com/user-attachments/assets/63096d78-9575-4a15-9dbc-b3464119c66f)

Повторим создание персонажа на примере бота, найдём анимацию `idle`, то есть, где персонаж стоит, откроем её как новую унаследованную сцену:

![image](https://github.com/user-attachments/assets/93ad031d-0963-45a6-a672-f3b21da0a20d)

На новой сцене открываем персонажа в редакторе:

![image](https://github.com/user-attachments/assets/e279b6db-b7ae-4b27-b76a-15211f46613e)

Выбираем `всё равно открыть` в появившемся окне:

![image](https://github.com/user-attachments/assets/eab730e9-dccf-4282-a88f-faec09ca07ae)

Изменяем тип персонажа на `CharacterBody3D`, переименовываем, добавляем `CollisionShape3D`:

![image](https://github.com/user-attachments/assets/3e755c05-7d02-420d-8332-fd311462c49d)

Далее добавляем персонажу все нужные анимации:\
\
(процесс добавления)\
\
После чего получаем вот такой результат:

![image](https://github.com/user-attachments/assets/0ae3c535-919e-4363-8849-d35142c56063)

Теперь бота можно добавить на сцену:

![21](https://github.com/user-attachments/assets/a40ae279-fa26-4f93-9325-70ee3146bead)

Найдём его и поменяем размер, чтобы бот смотрелся адекватно:

![image](https://github.com/user-attachments/assets/dd006892-0022-478a-a685-3bd22c1b197b)

Игра запущена, всё выглядит корректно:

![22](https://github.com/user-attachments/assets/a2ff877b-a0dd-465f-bcd1-b86b6b61cd30)

Пора приступать к настройке бота и к написанию скрипта для него.











