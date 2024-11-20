# Урок 3

## Краткое содержание
- Делаем поражение
- Делаем победу
- Рестарт игры
- Расширяем словарь

## Поражение

Если на прошлом уроке вы создали метод `set_game_over()`, то переходим к нему, а если нет, то создайте.

```gdscript
func set_game_over():
  	print("Поражение")
```
Давайте в случае поражения покажем игроку загаданное слово. Как это сделать можете спросить у учеников.
<br> Пишем строку, которая выведет в узел `Label` загаданное слово.

```gdscript
func set_game_over():
	$Control/Label.text = secret_word # выводим загаданное слово 
```

А в методе `add_wrong_letter()` добавляем строку, которая проверяет количество попыток и если их 0, то вызывает метод `set_game_over()`

```gdscript
func add_wrong_letter():
	tries -= 1
	$Control/TriesLabel.text = "Попыток: " + str(tries)
	bad.append(letter)
	$Control/BadLabel.text += letter + str(", ")
		
	if tries == 0: # если попыток 0
		set_game_over() # вызывается метод
```

Теперь мы хотим выводить для игрока сообщение, которое выведется на экран с уведомлением о поражении. Создаем `Label` и переименовываем его в что-то вроде `StateLabel`.


![image](https://github.com/user-attachments/assets/7da09384-59c8-4854-b784-4e89862d242a)


>[!Note]
>`StateLabel` мы еще будем использовать и для метода победы. Просто переопределим текст. Не забудьте очистить у `StateLabel` свойство `Text`, если вы вписывали туда слово для проверки шрифта.

```gdscript
func set_game_over():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПРОИГРАЛ" # выводим сообщение о проигрыше игрока
  	$Control/StateLabel.add_theme_color_override("font_color", Color(0.573, 0, 0.161)) # при необходимости через скрипт можете менять цвет шрифта (тут указан красный)
```

Проверяем. Видим, что выводится сообщение, но можно продолжать игру. Заблокируем игроку возможность добавлять буквы, блокируя `LineEdit` и `Button`.

```gdscript
func set_game_over():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПРОИГРАЛ"
	$Control/StateLabel.add_theme_color_override("font_color", Color(0.573, 0, 0.161))
	$Control/Button.disabled = true # блокируем Button
	$Control/LineEdit.editable = false # блокируем LineEdit
```
Теперь игроку запрещается работать с узлами. Можно приступать к функции победы.

## Победа

Функционал победы будет работать схожим образом, даже практически идентично, разве что меняется способ вызова этого метода.

Идем к методу `add_correct_letter()`, т.к. он выполняется тогдка, когда мы вводим правильную букву. Идея такая же, как с поражением.

В этом методе, при каждом его вызове - мы проверяем, а не победил ли еще игрок. Для этого вводим новую переменную `good_count`, которая будет хранить в себе счетчик правильных букв.

```gdscript
var tries = 6
var good_count = 0 # создаем новую переменную 
```
И теперь внутри метода `add_correct_letter()` добавляем счетчик:

```gdscript

func add_correct_letter():
	good.append(letter)
	$Control/Label.text = ""
	good_count = 0 # как мы обнуляем Label выше, так же обнуляем счетчик, чтобы каждый раз кол-во букв считалось заново
	for i in range(len(secret_word)):
		print("i = ", i , secret_word[i])
		if secret_word[i] in good:
			$Control/Label.text += secret_word[i]
			good_count += 1 # мы увеличиваем значение здесь, чтобы избегать повторов, когда в слове есть повторяющиеся буквы
		else:
			$Control/Label.text += "_ "
```

>[!Caution]
>#### Почему обнуляем `good_count`?
>
>Обнуление `good_count` необходимо для того, чтобы каждый раз при вызове функции начинать подсчет правильно угаданных букв с нуля. Это важно, потому что если бы мы не обнуляли его, то он продолжал бы увеличиваться с каждым вызовом функции, что привело бы к неправильному подсчету.
>#### А почему прибавляем `good_count` именно внутри условия?
>
>Прибавление к `good_count` происходит только внутри условия `if secret_word[i] in good`. Это означает, что мы увеличиваем счетчик только тогда, когда текущая буква из `secret_word` действительно присутствует в списке угаданных букв (`good`). Если буква не угадана, то мы не должны увеличивать счетчик, так как это не будет соответствовать количеству правильно угаданных букв.

Теперь, когда мы увеличиваем счетчик корректно - создаем проверку на победу игрока.

```gdscript
func add_correct_letter():
	good.append(letter)
	$Control/Label.text = ""
	good_count = 0
	for i in range(len(secret_word)):
		print("i = ", i , secret_word[i])
		if secret_word[i] in good:
			$Control/Label.text += secret_word[i]
			good_count += 1
		else:
			$Control/Label.text += "_ "
	if good_count == len(secret_word): # если счетчик равен длине загаданного слова, то вызывается метод победы
		set_win()
```
Ну, а скрипт самого `set_win()` достаточно идентичен `set_game_over()`.

```gdscript
func set_win():
	$Control/Label.text = secret_word # покажем игроку слово на всякий случай
	$Control/StateLabel.text = "ТЫ ПОБЕДИЛ" # сообщаем о победе
	$Control/StateLabel.add_theme_color_override("font_color", Color(1, 1, 1)) # можете задать цвет на свой вкус
	$Control/Button.disabled = true # так же выключаем интерфейс
	$Control/LineEdit.editable = false
```

Всё, теперь игрок еще и побеждает. Отлично. Но теперь надо перезапускать игру.

## Перезапуск игры

Добавляем `Timer` и сигнал `timeout` к скрипту.
В самом скрипте пишем следующее:

```gdscript
func _on_timer_timeout():
	get_tree().reload_current_scene() # получаем дерево и перезапускаем сцену
```

А вызываться `timer` будет в методах победы и поражения.

```gdscript
func set_win():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПОБЕДИЛ"
	$Control/StateLabel.add_theme_color_override("font_color", Color(1, 1, 1))
	$Control/Button.disabled = true
	$Control/LineEdit.editable = false
	$Timer.start() # здесь


func set_game_over():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПРОИГРАЛ"
	$Control/StateLabel.add_theme_color_override("font_color", Color(0.573, 0, 0.161))
	$Control/Button.disabled = true
	$Control/LineEdit.editable = false
	$Timer.start() # здесь
```
Теперь убедитесь, что игра перезапускается без багов.

## Расширяем словарь

Вы можете дать детям написать словарь самим или же можете воспользоваться генератором или ИИ.
Нужно что-то вроде этого: 

```gdscript
var dictionary = [
	"яблоко",
	"банан",
	"груша",
	"апельсин",
	"киви",
	"ананас",
	"мандарин",
	"вишня",
	"персик",
	"слива",
	"арбуз",
	"ежевика",
	"черника",
	"клубника",
	"манго",
	"лимон",
	"грейпфрут",
	"маракуйя",
	"фейхоа",
	"папайя"
]
# желательно детям показать, чтобы заполняли массив с новой строки каждое слово
# так проще заполнять его
```

Далее очищаем `secret_word`, пусть равняется пустой строке

```gdscript
var secret_word = ""
```
И теперь расширяем функцию `_ready()` с такого вида:

```gdscript
func _ready():
	for i in len(secret_word):
		print()
		$Control/Label.text += "_ "
```

До такого:

```gdscript
func _ready():
	randomize() # рандомим сид
	var number_word = randi_range(0, len(dictionary) - 1) # выбираем случайное слово и отнимаем 1
	secret_word = dictionary[number_word] # случайное слово равняется номеру элемента из списка, который хранит слово
	print(secret_word) # для проверки выводим
	for i in len(secret_word):
		print("i = ", i)
		$Control/Label.text += "_ "
```

Почему мы отнимаем 1 вот тут: `var number_word = randi_range(0, len(dictionary) - 1)`? Потому что `len()` вернет длину переменной, но работаем мы с элементами массива, который начинает отсчет с 0, а `len()` начинает отсчет с 1. Поэтому чтобы их выровнять мы пишем `-1`, чтобы возвращаемое значение и последний элемент в массиве означал одно и то же.

>[!Tip]
>

![image](https://github.com/user-attachments/assets/937c49de-2e54-4c26-b688-03c3018ab9ed)
> Скрин с приведенной ошибкой

Вы можете проверить, как это работает вписывая в `_ready()` строку с выводом слова `print(dictionary[подставьте число от 0 до длины массива - 1])`.
