# Урок 1 

## Краткое содержание 
- Создание базовых узлов
- Отрисовка карты, змейки и яблока через код


# Создание базовых узлов

Создаем необходимые базовые узлы:
- `Node2D` - `Game` (корневой узел)
- `Node2D` - `TileMapLayers` (родительский узел для `TileMapLayer`)
- `TileMapLayer` - `Background` (узел с картой)
- `TileMapLayer` - `SnakeApple` (узел с яблоками и змейкой) 

![image](https://github.com/user-attachments/assets/0d55655c-cd0e-432c-b300-57fc6625019e)

Желательно переименовать все узлы для лучшего взаимодействия с ними.

>[!Tip]
>Не забудьте сохранить сцену!

Теперь нужно создать `TileSet` у `Background` и выставить значения свойства `TileSize`:
- `x`: 80
- `y`: 80

И после этого добавляем спрайт фона для карты в `TileSet`
![image](https://github.com/user-attachments/assets/e7eb82b1-936a-408d-be8b-daaa236ecaad)
