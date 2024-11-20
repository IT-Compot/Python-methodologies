# Урок 1

## Краткое содержание

- Добавление основных узлов;
- Вывод загаданного слова;
- Проверка правильно введеной буквы.

# Добавление основных узлов

Сперва создаете главную сцену, где корневым узлом будет Node2D. Переименуйте его в что-то вроде `Game` и после прикрепляйте в качестве дочернего узла `Control`.

У `Control` должны быть дочерние узлы:
- `ColorRect`
- `Label`
- `LineEdit`
- `Button`


![image](https://github.com/user-attachments/assets/a0a8e2af-23d0-40a3-8f2f-46d5f52373e9)

Выравнивайте и меняйте цвета на свой вкус. В материалах проекта можете найти готовые темы и шейдеры. Примените их, особенно, если вы работаете с изиками. 

>[!Note]
>Применить тему можно, если перетащить материал темы в `Control` во вкладке `Theme` в свойство `Theme`. ![image](https://github.com/user-attachments/assets/634c48e4-8ac2-4607-8d69-5f37345928ef)


Если вы применили тему к `Control`, то в инспекторе темы сможете настроить каждый элемент отдельно: кнопки, надписи и т.д.

![image](https://github.com/user-attachments/assets/0186da65-0040-4ca2-9803-5821a21d0ea3)

Можете показать детям все настройки. Там в основном они отвечают за цвет и границы прямоугольников. С изиками - лучше ничего не трогать, кроме цвета.

Что касается `ColorRect`, то к нему можно применить шейдеры. В файлах их два: полосатый и со звездами.

![image](https://github.com/user-attachments/assets/02a3cade-4850-4963-b928-61447aac9ada)



> Для этого шейдера надо выбрать цвета: `Color One` и `Color Two`, скорость проигрывания: `Speed`, количество линий: `Line Count`, угол: `Angle` и "замыливание": `Blur`.

![image](https://github.com/user-attachments/assets/df4f8c11-dc69-415a-86cf-063579d6571b)

> А для шейдера `Stars` лучше кроме цвета самого `ColorRect` ничего не менять или оставьте это на последок, если останется время.


Как настроите тему - можно приступать к скрипту. Дайте ученикам самим застилизовать свои игры. Где-то минут 10 максимум на это.

## Скрипт
### Вывод загаданного слова
>[!Tip]
>Сначала можешь ознакомиться со всем скриптом, чтобы лучше понимать общий вектор работы.

<details>
  <summary>Скрипт целиком</summary>

  ```gdscript
extends Node2D

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


var secret_word = ""
var letter = ""


var good = []
var bad = []

var tries = 6
var good_count = 0


func _ready():
	randomize()
	var number_word = randi_range(0, len(dictionary) - 1)
	secret_word = dictionary[number_word]
	print(secret_word)
	for i in len(secret_word):
		print("i = ", i)
		$Control/Label.text += "_ "


func _input(event):
	if event is InputEventKey and event.is_pressed():
		$Control/LineEdit.grab_focus()


func _on_button_pressed():
	letter = $Control/LineEdit.text
	$Control/LineEdit.text = ""
	$Control/LineEdit.placeholder_text = "Буква"
	
	if len(letter) != 1:
		$Control/LineEdit.placeholder_text = "Только 1 букву"
		return
	
	if letter in secret_word:
		add_correct_letter()
	else:
		add_wrong_letter()
			
	print(good, " good")
	print(bad, " bad")


func _on_line_edit_text_submitted(new_text):
	letter = $Control/LineEdit.text
	$Control/LineEdit.text = ""
	$Control/LineEdit.placeholder_text = "Буква"
	
	if len(letter) != 1:
		$Control/LineEdit.placeholder_text = "Только 1 букву"
		return
	
	if letter in secret_word:
		add_correct_letter()
	else:
		add_wrong_letter()
			
	print(good, " good")
	print(bad, " bad")


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
	if good_count == len(secret_word):
		check_win()


func add_wrong_letter():
	tries -= 1
	$Control/TriesLabel.text = "Попыток: " + str(tries)
	bad.append(letter)
	$Control/BadLabel.text += letter + str(", ")
		
	if tries == 0:
		check_game_over()


func check_win():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПОБЕДИЛ"
	$Control/Button.disabled = true
	$Control/LineEdit.editable = false
	$Timer.start()


func check_game_over():
	$Control/Label.text = secret_word
	$Control/StateLabel.text = "ТЫ ПРОИГРАЛ"
	$Control/Button.disabled = true
	$Control/LineEdit.editable = false
	$Timer.start()


func _on_timer_timeout():
	get_tree().reload_current_scene()

  ```
  
</details>


Прикрепляем скрипт к корневому узлу `Node2D` и добавляем первую переменную: `secret_word`. 

```gdscript
var secret_word = "кот" # В этой переменной мы храним загадываемое слово
```
Далее давайте выведем вместо слова - нижние подчеркивания, чтобы скрыть само слово. Сколько будет букв в слове - столько и черточек.

>[!Tip]
>Ты можешь попробовать спросить у детей, как вывести количество букв в консоль, независимо от того сколько будет букв в загаданном слове. Конечно же через цикл `for`!

Создадим функцию `_ready()`, так как она вызывается однажды при запуске проекта и там циклом выводим количество букв в консоль и черточки в `Label`.

```gdscript
func _ready():
	for i in len(secret_word):
		print("i = ", i)
		$Control/Label.text += "_ "
```

Объясняем, что такое [`len()`](https://docs.godotengine.org/en/4.3/classes/class_@gdscript.html#class-gdscript-method-len). При выводе нижних подчеркиваний в `Label` - добавляем пробелы после черточек, чтобы они не склеились.

### Отображение загаданного слова

Чтобы можно было сразу отправлять текст - прикрепляем к скрипту сигнал `text_submitted` от `LineEdit` к нашему скрипту.

![image](https://github.com/user-attachments/assets/8e683b53-8023-49c4-912a-223fd6d8c1af)

Как добавили сигнал - создаем переменную в которой будем хранить букву.

```gdscript
var secret_word = "кот"
var letter = "" # добавляем новую переменную
```

Теперь в скрипте пишем:
```gdscript
func _on_line_edit_text_submitted(new_text): # этот сигнал будет вызываться при нажатии на Enter
	letter = $Control/LineEdit.text  # записываем в переменную букву из LineEdit
	$Control/LineEdit.text = "" # очищаем сам LineEdit
	$Control/LineEdit.placeholder_text = "Буква" # Вписываем в PlaceHolder слово "Буква", чтобы игроку было понятнее, что вводить

	if len(letter) != 1: # если игрок будет вводить не 1 букву, то будет срабатывать скрипт ниже
		$Control/LineEdit.placeholder_text = "Только 1 букву" # в PlaceHolder напишется ввести 1 букву
		return # программа выйдет из условия в общий поток
```

Теперь проверьте, что игрок не может ввести больше одной буквы. Если детей будет не устраивать, что чтобы что-то написать - надо нажимать на `LineEdit`, то в допах можете посмотреть, как это исправить.

Как напишете скрипт следует добавить два массива, один для "правильных" букв, а второй для "неправильных". 

```gdscript
var good = [] # массив с "хорошими" буквами, которые есть в слове
var bad = [] # массив с "плохими" буквами, которых нет в слове
```


>[!Tip]
>Для того, чтобы нагляднее показать, как работает массив - можете скинуть этот [сайт](https://array-3d-viz.vercel.app/) или показать у себя на демке

Как разобрались и создали массивы - добавляем скрипт на проверку буквы в слове. Если буква есть в слове, то вызывается метод `add_correct_letter()`, а если буквы нет - `add_wrong_letter()`.
Сперва создайте пустые методы:
```gdscript
func add_correct_letter():
	pass
	

func add_wrong_letter():
	pass

```

Далее можете переходить обратно к методу `func _on_line_edit_text_submitted(new_text):` и пишем следующее условие:

```gdscript
	if letter in secret_word: # если буква есть
		add_correct_letter() # вызываем этот метод
	else: # иначе
		add_wrong_letter() # вызываем этот
			
	print(good, " good") # выводим в консоль массивы и подписываем их для проверки, но только после добавления методов
	print(bad, " bad")
```

### Добавление "хороших" букв

Теперь идем обратно к методу `add_correct_letter():`
И пишем следующий скрипт:
```gdscript
	good.append(letter) # добавляем букву в список хороших
	$Control/Label.text = "" # очищаем Label
	for i in len(secret_word): # цикл для отрисовки букв
		print("i = ", i , secret_word[i]) # для проверки
		if secret_word[i] in good: # проверяем есть ли у слова элемент i в массиве
			$Control/Label.text += secret_word[i] # добавляем букву, если есть
		else:
			$Control/Label.text += "_ " # добавляем обратно нижнее подчеркивание
```

Давай тут поподробнее
```gdscript
		if secret_word[i] in good: 
			$Control/Label.text += secret_word[i] 
		else:
			$Control/Label.text += "_ " 
```

У нас есть цикл `for`, который пробегается по слову. Начинается отсчет с 0 и идет до конца слова. Например, в слове "кот" 3 символа, а значит 3 элемента, которые начнут отсчет с 0.
- `0` - к
- `1` - о
- `2` - т
Этот цикл проходит по всем индексам букв в `secret_word`. Мы используем `range(len(secret_word))`, чтобы получить индексы от 0 до длины слова минус один.

```gdscript
   if secret_word[i] in good:
```
И в условии мы берем слово и в квадратных скобках указываем номер элемента, номер буквы другими словами. Здесь мы проверяем, есть ли текущая буква (например, "о") в массиве `good`. Если да, значит, буква была угадана.

Если угадана буква, то обновляем `Label` и добавляем букву:

```gdscript
if secret_word[i] in good: 
	$Control/Label.text += secret_word[i] 
```
А остальные не угаданные буквы возвращаем в виде нижних подчеркиваний:

```gdscript
else:
	$Control/Label.text += "_ " 
```
>[!Note]
>По факту мы перерисовываем каждый раз загаданное слово, но с учетом правильных букв.

### Добавление "плохих" букв

Тут всё просто: добавляете в метод `add_wrong_letter()` одну строчку
```gdscript
func add_wrong_letter():
	bad.append(letter) # добавляем в массив "плохих" букв
```


# Итоги

1) Есть основа игры
2) Изучили принцип работы массивов
3) Научились через цикл выводить буквы и нижние подчеркивания вместо букв
4) Можно угадать слово, но пока без проигрыша или выигрыша 
