# Python: Основы. Урок 3

**Цель урока**: Познакомиться с ключевыми элементами языка Python: циклы.

## 1. Разбираемся, как работают циклы

Работать над этим и последующими проекта продолжаем в Pycharm.

Разбираем несколько простых примеров ниже.

**Пример 1**

```python
text = "python"

for letter in text:
  print(letter)
```

>[!TIP]
>Цикл -

**Пример 2**

```python
number = int(input("Enter the number: "))

for i in range(1 ,15):
  total = number * i
  print(number, "*", 1, "=", c)
```

**Пример 3**

```python
number = int(input("Enter the number: "))

for i in range(0, number + 1):
  for j in range(i):
    print(i, end = "")
  print()
```

**Пример 4**

```python
for i in range(0, 5):
  print(i)
else:
  print("Loop is ended.")
```

**Пример 5**

```python
for i in range(1, 11):
  if i == 5:
    break  # Прерываем цикл, когда i равно 5
  print(i)

print("Цикл завершен.") # Эта строка выполнится после выхода из цикла
```

>[!TIP]
>**Оператор в Python** – это символ или комбинация символов, которые выполняют определенную операцию над данными (операндами). Операторы могут быть арифметическими (например, `+`, `-`, `*`, `/`), логическими (`and`, `or`, `not`), операторами сравнения (`==`, `!=`, `>`, `<`), операторами присваивания (`=`), и другими.
>
>`break` - это оператор, который прерывает выполнение цикла (`for` или `while`) и передает управление следующей инструкции после цикла.

**Пример 6**

```python
food = ["пицца", "суши", "торт"]

for i in food:
  if i == "пельмени":
    print("Не хочу.")
    break
  print("О, " + i + " сюда!")
else:
  print("Хорошо, что в этот раз без пельменей")
print("Обед закончился.")
```

**Пример 7**

```python
string = "point"
i = 0

while i < len(string):
  if string[i] == "i" or string[i] == "n":
    i += 1
    countinue
  print(string[i])
  i += 1
```
