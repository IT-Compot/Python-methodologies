# Урок 2

## Краткое содержание
- Создание пули
	- [Скрипт пули](#перейдем-к-скрипту)
- [Снова работаем с игроком](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/lessons/lesson-2.md#%D0%B2%D0%B5%D1%80%D0%BD%D0%B5%D0%BC%D1%81%D1%8F-%D0%BA-%D0%B8%D0%B3%D1%80%D0%BE%D0%BA%D1%83)
	- Работаем со [скриптом](#перейдем-к-скрипту) игрока 
- [Итоги](https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/lessons/lesson-2.md#%D0%B2%D0%B5%D1%80%D0%BD%D0%B5%D0%BC%D1%81%D1%8F-%D0%BA-%D0%B8%D0%B3%D1%80%D0%BE%D0%BA%D1%83)


### Создание пули
<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/bullet_pic.jpg" id="bullet_pic">

Создаем новую сцену и в качестве корневого узла используем `Area2D`.


Базово для создания пушки потребуются следующие узлы:

* `Area2D` - пули у нас будут сделаны из узла области
* `MeshInstance2D` - это узел, который позволяет вам отображать 2D-меши (сеточные объекты) в 2D-пространстве
* `CollisionShape2D` - узел коллизии
* `VisibleOnScreenNotifier2D` - это узел, который позволяет отслеживать, виден ли объект на экране камеры

Начнем с настройки меша. Вообще `MeshInstance2D` полезен, когда вам нужно отобразить 2D-объекты с высокой детализацией или когда вы хотите использовать возможности 3D-графики в 2D-контексте, но в нашем случае можно просто сделать 2D-сферу и использовать её в качестве пули.

В параметре `Mesh` выбираем фигуру, а потом подбираем по размеру. 
>[!Tip]
>Можете добавить копию меша на сцену игрока или наоборот добавить игрока в сцену с пулей, чтобы посмотреть на пропорции.

Пример на скрине ниже:

<img src="https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/mesh_screenshot.jpg">

Добавляем форму коллизии и настраиваем область `VisibleOnScreenNotifier2D` и получим что-то вроде [этого](#bullet_pic)



#### Перейдем к скрипту

Для начала взглянем на полный скрипт пули

```gdscript
extends Area2D  # Наследуемся от Area2D (объект, который может реагировать на столкновения)

const SPEED := 800  # Константа скорости движения (800 пикселей в секунду)

var direction: Vector2 = Vector2.ZERO  # Вектор направления движения, изначально (0,0)

func _physics_process(delta: float) -> void:
    # Определяем направление движения, основываясь на текущем угле поворота (rotation)
    var direction: Vector2 = Vector2.RIGHT.rotated(rotation)  

    # Перемещаем объект в направлении `direction` с учётом скорости и времени кадра
    position += direction * SPEED * delta

func _on_body_entered(body):
	queue_free()  # Уничтожить пулю при столкновении

func _on_visible_on_screen_notifier_2d_screen_exited(): # Метод вызывается, если пуля покидает поле зрения камеры
	print("bullet is deleted")
	# удаляем пулю
	queue_free() 
```

Теперь построчно и начнем с основного: движение пули.

```gdscript
const SPEED := 800 # можно использовать сокращенную форму статической типизации
var direction: Vector2 = Vector2.ZERO  # или можно указать тип 

func _physics_process(delta: float) -> void:
    var direction: Vector2 = Vector2.RIGHT.rotated(rotation)  
    position += direction * SPEED * delta
```

>[!important]
>Укажите на хоть и незначительную, но все же разницу в указании типов данных при объявлении переменной. Вариант `:=` более короткий в записи, а `var example : int = 5` более подробный и точный.


1. `extends Area2D`
Этот код указывает, что наш скрипт наследуется от Area2D – специального узла, который используется для обработки столкновений и зон триггеров. Это значит, что объект с этим скриптом может реагировать на пересечения с другими объектами (например, наш случай, пуля может пересекать врагов).

2. `const SPEED := 800`
Объявляется константа `SPEED`, которая задаёт скорость движения объекта.

`const` означает, что значение нельзя изменить во время работы игры.
`:=` – сокращённая форма присваивания и указания типа. Двоеточие задаёт тип переменной. Если тип не указан, `Godot` попытается его вывести автоматически.

| Особенность            | Статическая типизация (`: тип`)         | Динамическая типизация (`var`)       |
|------------------------|---------------------------------|--------------------------------|
| **Объявление переменной** | `var speed: int = 10`         | `var speed = 10`               |
| **Безопасность типов**  | Проверяется **на этапе компиляции**, меньше ошибок в рантайме | Ошибки возможны **во время выполнения** |
| **Производительность**  | Быстрее, так как тип известен сразу | Чуть медленнее, так как тип проверяется в рантайме |
| **Гибкость**           | Жёстко определённый тип, нельзя изменить (`int` → `string` вызовет ошибку) | Можно изменить тип в любой момент (`speed = "fast"`) |
| **Автодополнение (IntelliSense)** | Работает лучше, так как Godot знает точный тип | Может работать хуже, так как тип неизвестен |
| **Отладка**            | Легче находить ошибки типов | Возможны неожиданные ошибки, если тип изменился |
| **Использование в GDScript** | Рекомендуется для **критичных участков кода**, например, в физике или AI | Удобно для **гибких данных**, например, в UI или JSON |
| **Пример использования** | `var health: int = 100` (не изменится на `string`) | `var player_data = { "name": "Hero", "score": 10 }` |


3. `var direction: Vector2 = Vector2.ZERO`
Создаётся переменная `direction`, которая хранит направление движения в виде двумерного вектора `(Vector2)`.

`Vector2.ZERO` – это `(0, 0)`, то есть объект изначально не движется.

4. `func _physics_process(delta: float) -> void:`
Функция `_physics_process(delta)` выполняется каждый кадр, но с учётом физического времени, чтобы движение было плавным, даже если FPS меняется.
`delta` – время, прошедшее с прошлого кадра (например, 0.016 секунд при 60 FPS).
`-> void` означает, что функция ничего не возвращает.

5. `var direction: Vector2 = Vector2.RIGHT.rotated(rotation)`
`Vector2.RIGHT` – это (1, 0), то есть вектор, направленный вправо.
`.rotated(rotation)` – поворачивает этот вектор на угол `rotation` объекта. <br>
Что это даёт?
Это позволяет объекту двигаться в направлении его поворота. Например:<br>
- Если `rotation = 0`, `direction` остаётся `(1, 0)` (движение вправо).
- Если `rotation = 90°` (или `PI/2` в радианах), вектор `direction` будет `(0, 1)` (вниз).

6. `position += direction * SPEED * delta`
`direction * SPEED` – получает вектор скорости, умножая направление на скорость (`Vector2` * число умножает оба компонента `X` и `Y`).
`* delta` – делает движение зависимым от времени, чтобы объект перемещался равномерно независимо от `FPS`.
`position += ...` – перемещает объект на рассчитанное расстояние.

Что делает этот код?<br>
Объект движется в направлении своего поворота (`rotation`) с постоянной скоростью 800 px/с.
Движение не зависит от `FPS`, потому что используется `delta`.

Теперь добавляем сигналы от узлов `Area2D` и `VisibleOnScreenNotifier2D`.

```gdscript
func _on_body_entered(body): # сигнал от Area2D, срабатывает при попадании тела в область
	queue_free()  # Уничтожить пулю при столкновении

func _on_visible_on_screen_notifier_2d_screen_exited(): # сигнал вызывается, если пуля покидает поле зрения камеры
	print("bullet is deleted")
	# удаляем пулю
	queue_free() 
```

Добавить сигналы можно во вкладе `Узел` в правом верхнем углу, возле `Инспектор`.

# Вернемся к игроку

Добавим игроку новые узлы: `Marker2D` и `AudioStreamPlayer2D`, переименуем их в `ShotPoint` и `ShotSound` или что-то вроде того.<br>

### Поработаем с новыми узлами
Маркер добавляем примерно напротив игрока, вот так (подсвечен перекрестием):
<img src='https://github.com/IT-Compot/Python-methodologies/blob/main/first-stage/Shooter/images/marker2d_player.jpg'>

>[!Tip]
>`Marker2D` в `Godot Engine` используется для обозначения определенных точек или мест в 2D-пространстве. Он может служить нескольким целям:
>1. Навигация: `Marker2D` можно использовать для установки меток на пути, которые могут быть полезны для навигации `NPC` или других объектов.<br>
>2. Точки спавна: Вы можете использовать `Marker2D` для указания мест, где могут появляться объекты или персонажи в игре.<br>
>3. События: `Marker2D` может служить триггером для различных событий, таких как активация анимаций, изменение состояния игры или запуск каких-либо действий.<br>
>4. Упрощение разработки: Он помогает разработчикам визуально организовывать уровень, добавляя метки, которые облегчают понимание структуры сцены.<br>

Добавляем звук выстрела в `ShotSound` в параметр `Stream`

### Переходим к скрипту

```gdscript
var is_can_fire := true # переменная, которая проверяет может ли игрок стрелять
var bullet_area = preload("res://Scenes/Entity/bullet_area.tscn") # предзагружаем сцену пули (путь может отличаться)
#... 
func shoot():
	if is_can_fire:  # если игрок может стрелять
		var bullet_instance = bullet_area.instantiate()  # создаем экземпляр пули
		$ShotSound.play() # проигрываем звук выстрела
		bullet_instance.global_position = $ShotPoint.global_position  # синхронизируем глобальную позицию образца пули и точки выстрела 
		bullet_instance.global_rotation = $ShotPoint.global_rotation  # синхронизируем глобальное вращение образца пули и точки выстрела 
		get_parent().add_child(bullet_instance) # получаем родителя текущего узла и добавляем пулю
		is_can_fire = false # не можем стрелять
		await get_tree().create_timer(0.2).timeout # создаем таймер и ждем сигнала окончания таймера
		is_can_fire = true # можем стрелять
```
Все что нам осталось это добавить кнопку которая будет отвечать за стрельбу и создать условие нажатия действия для выстрела. Назвать можете `fire`, `shot` и все в таком духе.
```gdscript
func _physics_process(delta):
#...
	if Input.is_action_pressed("fire"):
		shoot()
```

# Итоги
- Готовая механика стрельбы
- Научились создавать объекты в игре

