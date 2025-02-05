# Урок 1

## Краткое содержание
- Создание карты
- Добавление персонажа

# Создание карты

Здесь всё, как и прежде - карту делаем через `TileMapLayer` :shipit:

Узлы для создания карты:
- `TileMapLayer` - основная карта
- `ColorRect` - узел, чтобы закрасить серый фон

Создадим карту с физическими слоямии и сразу же со слоями навигации для ботов. Для этого создаем `TileMapLayer`. В свойствах `TileMap` создаем `TileSet` после чего у нас появится сетка игрового поля. <br>
Значения у `TileSize` выставляем: `x: 32`, `y: 32` <br>


Добавляем наш набор тайлов, он должен выглядить примерно так:

![image](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/tile_pack.jpg)

>[!Tip]
>Если используешь этот же ассет пак, то проще будет сделать стенкой - белые тайлы и полом - черные тайлы

Теперь создаем `Physics Layer` и `Navigation Layer`. Необходимо выбрать `TileMapLayer` и в параметрах открыть соответствующие вкладки. Подробнее на скрине:

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/tilemaplayer_parameters.png">

Теперь нужно добавить слои навигации и физический слой на тайлы. По навигационным тайлам будут ходить боты, а физические тайлы нужны для столкновения.

>[!Important]
>Для физических слоев навигационный слой не делаем, иначе боты будут пытаться ходить по этим тайлам

#### Физический слой:

![image](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/HowToMakeCollisions.gif)

>[!Tip]
>Нажми на галочку на гифке, чтобы включить её

#### Навигационный слой:

![image](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/HowToMakeNavTile.gif)

Теперь даем волю фантазии и рисуем карту по которой будет перемещаться игрок. Дайте ученикам порисовать их арену. Пусть попробуют спроектировать арену с учетом спавна врагов со всех сторон. Помогайте им

#### Пример арены:

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/ArenaExample.jpg">

И напоследок можно добавить узел `ColorRect`, чтобы закрасить фон. Цвет подберите на свой вкус и расстяните за пределы экрана, чтобы не было видно серый фон

# Создание игрока

Для начала создадим `CharacterBody2D` и доабвим к нему следующие узлы:
* `Sprite2D` - для персонажа
* `CollisionShape2D` - для коллизий
* `Camera2D` - камера

>[!Important]
>Переименовывайте узлы! Так ученикам будет понятнее с чем они работают и проще запомнить. Коллизии можно не переименовывать (их можно отследить по контексту того к кому они подключены, но при желании тоже можете), а вот `Marker2D` можно переименовать в `ShotPoint`, `Area2D` в `HurtBox`, `AudioStreamPlayer2D` в `ShotAudio2D` или что-то вроде такого.

Добавим сразу все необходимые узлы, а настройкой займемся по порядку.

В `Sprite2D` в параметр `Texture` добавляем нужный спрайт игрока.  

Получится что-то вроде такого:

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/player_screen_shot.png">

И прокидываем все уже известные параметры для коллизий. 

- Создаем круглую коллизию для `CollisionShape2D` самого игрока
- Такую же круглую коллизию для `CollisionShape2D`, которая внутри `Area2D`
- Ставим `Marker2D` правее игрока

И получается что-то вроде такого:

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/player_with_collisions.jpg">

>[!Tip]
>Для удобства можете поменять цвета для коллизий.

Добавим анимацию игроку
![image](https://github.com/Sindikaty/byteschool/assets/158248099/c6f65643-f853-440c-89d2-f967d14b4dd1)

### Переходим к работе со скриптом

Сначала зададим перемещение. Для этого создадим 2 переменные отвечающие за скорость и вектор движения

```gdscript
@export var speed : int = 100
var input_vector = Vector2.ZERO
```

После чего зададим само пермещение, а также проигрыванеи анимаций

```gdscript
func _physics_process(delta):
  input_vector.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	input_vector.y = Input.get_action_strength("down") - Input.get_action_strength("up")
	
	velocity = input_vector * speed

	if(input_vector.x > 0):
		$AnimatedSprite2D.play("run")
		$AnimatedSprite2D.flip_h = false
	elif(input_vector.x < 0):
		$AnimatedSprite2D.flip_h = true
		$AnimatedSprite2D.play("run")
	move_and_slide()
```
Ниже пойдет скрипт, необходимый для осуществления поворота персонажа

```gdscript
func _physics_process(delta):
        ...
	var mouse_pos = get_global_mouse_position() # - получаем позицию мыши
	look_at(mouse_pos) # - персонаж смотрит на курсор (мышь)
	$AnimatedSprite2D.global_rotation = 0.0 # - блокирует возможность вращения текстуры персонажа (если в этом есть необходимость)
```

> [!CAUTION]
> Методы написания скрипта может отличаться в зависимости от текстур, которые вы используете. Некоторые текстуры может быть необходимо вращать, а некоторые - нет. Будьте внимательны и готовы к такому

Так как мы делаем шутер можно добавить удобный прицел. Для этого создадим еще одну переменную

```gdscript
var cursor = preload("res://textures/white_crosshair.png")
```

```gdscript
func _physics_process(delta):
  ...  
  Input.set_custom_mouse_cursor(cursor, Input.CURSOR_ARROW, Vector2(16,16))
```

>[!IMPORTANT]
> Обрати внимание на путь, где лежит текстура. У вас может немного отличаться, но лучше все разбивать на отдельные папки


#### Создание деша
Фрагмент кода ниже нужен для создания деша (ускорения)

![](https://github.com/mykweenn/byteschool/blob/main/shooter/img/tumblr_nemrsjk8hi1sulisxo1_1280.webp)

> У нас будет не так красиво выглядеть деш, но по механике будет так работать

Создадим переменные которые нам понадобятся чуть позже

```gdscript
var dash_trigger = false
var dash_time = 0
```

Теперь создадим функцию рывка
```gdscript
func dash(delta):
	transform.origin = lerp(transform.origin, transform.origin + 40 * input_vector , 0.1)
```

Этот код означает следующее:

* transform.origin - это позиция объекта в пространстве.
* lerp() - это функция, которая выполняет линейную интерполяцию между двумя значениями. В данном случае, она применяется к текущей позиции объекта и новой позиции, которая получается при добавлении вектора управления (input_vector), умноженного на 40 .
* 0.1 - это коэффициент сглаживания, который определяет, насколько быстро объект будет перемещаться к новой позиции.
Таким образом, этот код перемещает объект с текущей позиции к новой позиции, которая получается при добавлении вектора управления, умноженного на 40, с использованием линейной интерполяции для плавного перемещения.

Ниже представлен метод, в котором написаны условия для применения деша

```gdscript
func get_input_velocity(delta): # В аргумент
	if Input.is_action_just_pressed("dash"): # Если нажата кнопка деша, то...
		dash_trigger = true # срабатывает триггер деша
	if dash_trigger == true: # если триггер деша равен истине, то
		dash_time += delta # к дешу прибавляется delta (таким образом создается локальный таймер)
		dash(delta) # вызываем функцию деша, которую вы писали ранее
		if dash_time > 0.25: # Если время деша превышает 0.25 секунды, то
			dash_trigger = false # вырубаем деш
			dash_time = 0 # время деша откатывается к 0
```
Все что нам остается это добавить вызов функции в методе `_physics_process(delta)`

```gdscript
get_input_velocity(delta)
```
И последним что мы сделаем в этом уроке, добавим прицеливание. Для его создания нам понадобится `Marker2D`

![image](https://github.com/Sindikaty/byteschool/assets/158248099/0ab3e2fc-1f94-4943-8e0f-aea472e5e4ac)

Создадим новую функцию `scope`
```gdscript
func scope():
	if Input.is_action_pressed("aim"): # При зажатии ПКМ срабатывает одно из условий ниже
		$Camera2D.position = $scope.position # Если нажат ПКМ, то камера перейдет к позиции прицела
	else:
		$Camera2D.position = Vector2(0,0) # Иначе камера сместится обратно в начальную позицию
```
И добавим ее вызов функции в методе `_physics_process(delta)`
