# 3 Урок - Квестгивер

## Цель урока
Создание персонажа дающего задания, познакомиться с `зелёными узлами` предназначенными для GUI.

## Визуальная часть
Следующий подраздел начнем с создания персонажа у которого мы можем получить квест.
![изображение](https://github.com/user-attachments/assets/278c1a7d-d11e-4744-94f2-6b0f0d23f00b)
На картинке изображены все необходимые узлы для визуального отображения персонажа на сцене. Дайте вашим ученикам возможность самостоятельно настроить свойства для этих узлов. Здесь ваша задача лишь направлять.

## Диалоговое окно
Набор узлов будет зависеть в первую очередь от того, что придумают ваши ученики. Здесь в примере будет стандартное диалоговое окно, однако не стесняйтесь давать вашим ученикам творческий простор.
Вот список узлов которые вам потребуеются:
- `CanvasLayer` - для того чтобы закрепить диалоговое окно на экране viewport.
- `Control` - для того чтобы сгрупировать всё диалоговое окно в целом.
- `Pnael` - для фона и дополнительного оформления.
- `AnimatedSprite2D` - для создания анимированной иконки.
- `Lable` - здесь будет отображатся текст квест гивера.
- `Button` - для выбора опций.

#### Итоговый примерный вариант с наименованиями узлов:
![изображение](https://github.com/user-attachments/assets/2678fac9-612c-489b-aa1b-3f3a9427f1a6)

### Скрипт 
Перед тем как вы начнёте писать скрипт давайте сделаем `уникальное имя` для квест гивера. Сделать это можно нажав по узлу `QuestsGiverWindow` <b>правой кнопкой мыши</b>, затем в появившемся окне выбрать `% Доступ как к уникальному имени`. 
![unickname](https://github.com/user-attachments/assets/3625fada-477d-4b51-b500-08b65e2ce8df)

>[!TIP]
>Уникальные имена узлов сокращают путь обаращения к ним и улучшают читаемость и безопасность вашего кода. Однако пользоваться ими нужно с умом, не стоит давать уникальные имена всем узлам подряд.

### Логика появления диалогового окна
- Прикрепите скрипт к узлу `QuestGiverWindow`
- Выберите в <b>фильтре узлов</b> `Area2d` и в разделе `Узел` прикрепите 2 сигнала `body_entered` и `body_exited` к узлу `QuestGiverWindow`.
![signals](https://github.com/user-attachments/assets/8f4b04cd-5175-4df9-bade-a879e5a4e185)

Остаётся только написать скрипт появления диалогового окна:
```gdscript
extends Control


var in_area = false

func _on_option_1_pressed() -> void:
	$Background/QuestText.text = "Отлично! Я хочу попросить тебя найти мой ус креветки! Найди мне его!"


func _on_quit_dialog_pressed() -> void:
	in_area = false

func _process(delta: float) -> void:
	if in_area:
		visible = true
	else:
		visible = false

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.name == 'Player':
		in_area = true


func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.name == 'Player':
		in_area = false
```

Итоги урока:
- Получен опыт работы с узалми для вёрстки
- Узанли о уникальных именах `%`
- Повторили как работать с сигналами от узлов
