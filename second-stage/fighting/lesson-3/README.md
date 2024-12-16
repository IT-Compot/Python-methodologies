# Файтинг | Урок 3

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

## Скрипт бота 

### База бота

Приступаем к созданию логики для бота и написанию скрипта для него. Скрипт прикрепяем обязательно внутри самой сцены бота, а не к узлу бота на карте:

![image](https://github.com/user-attachments/assets/1a965114-fe9d-4541-86f0-fb1291004bc6)

Шаблон также не потребуется:

![image](https://github.com/user-attachments/assets/9221c723-1c87-4c3c-a952-6fa92653bba7)

Скрипт создан, теперь подумаем какие параметры нам потребуются? Их можно скопировать из скрипта персонажа.\
Конечно, это скорость и текущая анимация. Добавим также функцию _ready() чтобы при запуске игры всегда запускалась анимация `idle`:

![image](https://github.com/user-attachments/assets/f6d52794-3a52-496c-9364-139aa73be108)

Также заберём функцию _physics_process(delta), но уберём из неё неиспользуемые функции:

![image](https://github.com/user-attachments/assets/816b569b-d420-42a6-b644-fafc99e5ab93)

Функция animation() нам нужна, поэтому тоже скопируем её в скрипт бота и адаптируем под текущий код и существующие у бота анимации:

![image](https://github.com/user-attachments/assets/c5a64e96-de44-469b-bcfa-a6859395e362)

Также не забудем про функцию, которая сбрасывает анимации, когда одна из них закончилась:

![image](https://github.com/user-attachments/assets/3aacddc5-a381-40a4-afd4-871849922bec)

Получился следующий скрипт:

```GDScript
extends CharacterBody3D

var action = 'none'

const SPEED = 5.0

func _ready() -> void:
	$AnimationPlayer.play("idle")
	
	
func _physics_process(delta: float) -> void:

	if not is_on_floor():
		velocity += get_gravity() * delta

	animation()
	move_and_slide()
	
func animation():
	match action:
		"punch":
			$AnimationPlayer.play("punch")
		"kick":
			$AnimationPlayer.play("kick")
		"recieve_damage":
			$AnimationPlayer.play("recieve_damage")
		"forward":
			$AnimationPlayer.play("forward")
		"none":
			$AnimationPlayer.play("idle")
		"die":
			$AnimationPlayer.play("dying")
			

func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	if anim_name == "punch":
		action = "none"
	elif anim_name == "kick":
		action = "none"
	elif anim_name == "recieve_damage":
		action = "none"
	elif anim_name == "forward":
		action = "none"
```

Готово. База готова, теперь напишем логику его поведения.

### Интеллект бота




