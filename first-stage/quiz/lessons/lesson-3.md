# Урок 3

## Краткое содержание
- Делаем поражение
- Делаем победу
- Рестарт игры

## Поражение

Если на прошлом уроке вы создали метод `check_game_over()`, то переходим к нему, а если нет, то создайте.

```gdscript
func check_game_over():
  print("Поражение")
```
Давайте в случае поражения покажем игроку загаданное слово. Как это сделать можете спросить у учеников.
<br> Пишем строку, которая выведет в узел `Label` загаданное слово.

```gdscript
func check_game_over():
	$Control/Label.text = secret_word # выводим загаданное слово 
```

А в методе `add_wrong_letter()` добавляем строку, которая проверяет количество попыток и если их 0, то вызывает метод `check_game_over()`

```gdscript
func add_wrong_letter():
	tries -= 1
	$Control/TriesLabel.text = "Попыток: " + str(tries)
	bad.append(letter)
	$Control/BadLabel.text += letter + str(", ")
		
	if tries == 0: # если попыток 0
		check_game_over() # вызывается метод
```

Теперь мы хотим выводить для игрока сообщение, которое выведется на экран с уведомлением о поражении. Создаем `Label` и переименовываем его в что-то вроде `StateLabel`.

>[!Note]
>`StateLabel` мы еще будем использовать и для метода победы. Просто переопределим текст.

```gdscript
func check_game_over():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПРОИГРАЛ" # выводим сообщение о проигрыше игрока
  $Control/StateLabel.add_theme_color_override("font_color", Color(0.573, 0, 0.161)) # при необходимости через скрипт можете менять цвет шрифта (тут указан красный)
```

Проверяем. Видим, что выводится сообщение, но можно продолжать игру. Заблокируем игроку возможность добавлять буквы, блокируя `LineEdit` и `Button`.

```gdscript
func check_game_over():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПРОИГРАЛ"
	$Control/StateLabel.add_theme_color_override("font_color", Color(0.573, 0, 0.161))
	$Control/Button.disabled = true # блокируем Button
	$Control/LineEdit.editable = false # блокируем LineEdit
```
