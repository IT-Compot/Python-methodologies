# Допы по Квизу

# Музыка и звуки

Создайте узел `Node` и сложите туда все узлы `AudioStreamPlayer`. 
Вы можете добавить фоновую музыку, звуки угадывания буквы, звук неправильной буквы, звук победы и поражения.

![image](https://github.com/user-attachments/assets/e84a6ea6-61ea-40f9-bd66-3295ab5e7a7c)
>Для чистоты дерева узлов - сортируем их так.

Теперь вызываете каждый звук в нужном контексте. Фоновую музыку можно включать сразу, используя свойство `autoplay` в  инспекторе `AudioStreamPlayer` или в скрипте при загрузке игры прописать: 

#### Фоновая музыка
```gdcript
func _ready():
	$AudioNode/AudioBackground.play() # пишем в начале или в конце функции ready, как вам удобнее
```

#### Правильная буква
```gdscript
func add_correct_letter():
	$AudioNode/AudioCorrect.play()
```

#### Неправильная буква
```gdscript
func add_wrong_letter():
	$AudioNode/AudioWrong.play()
 ```

#### Победа
```gdscript
func set_win():
	$AudioNode/AudioWin.play()
```

#### Поражение
```gdscript
func set_game_over():
	$AudioNode/AudioLose.play()
```
