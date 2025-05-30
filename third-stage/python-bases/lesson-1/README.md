# Python: Основы. Урок 1

**Цель урока:** Познакомиться с ключевыми элементами языка Python: переменные, условные операторы (`if`, `elif`, `else`) и создание функций.

## 1. Выбираем среду разработки

Для начала работы с Python нам понадобится среда, где мы сможем писать и запускать код.  Самый простой способ - воспользоваться онлайн-интерпретатором. Они не требуют установки и доступны прямо в браузере.

Вот несколько рекомендуемых вариантов:

*   [Online Python](https://www.online-python.com/) - Отличный выбор для новичков, простой и понятный интерфейс.
*   [Python Sandbox](https://pythonsandbox.com/) - Еще одна удобная платформа для экспериментов с кодом.

*Важно!* Убедитесь, что все ученики имеют доступ к выбранному сайту и могут запускать код.

## 2. Вывод данных. Функция `print`

>[!TIP]
>Функция print() - одна из самых важных и часто используемых в Python. Она позволяет выводить информацию на экран (в консоль). Вы можете выводить текст, числа, значения переменных и даже результаты вычислений.

Показываем несоклько вариантов использования фукнции `print`.

```python
print("Hello, world!")
print(hello)
print(2 + 4)
print("I am " + 13)
print("I am " + str(13))
print("I am " + "13")
```

## 3. Переменные. Хранение данных

Теория о переменных

Пример 1:

```python
name = "Ivan"
print(name)
name = "Vadim"
print(name)
```

Пример 2:

```python
num_1 = 5.5 # float
num_2 = 3   # int

print(num_1 + num_2)
```

Немного дополянем пример 2

Пример 3:

>[!CAUTION]
>В примере ниже показана ошибка, что будет, если сложить `str` и `int `

```python
num_1 = 5.5 # float
num_2 = 3   # int
num_3 = "4" # str

print(num_1 + num_3)
```

Исправленный вариант:

```python
num_1 = 5.5 # float
num_2 = 3   # int
num_3 = "4" # str

print(num_1 + int(num_3))
```

## 4. Условные операторы

Разбираем основные элементы Python на нескольких простых примерах.

Приводим ученикам простой пример о том, как работают условыне операторы и всё объесняем. С доп. информацией по условным операторам можно ознакомиться здесь [условные операторы в Python](https://skillbox.ru/media/code/uslovnye-operatory-v-python-ot-prostykh-esli-do-vlozhennykh-konstruktsiy/?ysclid=m7uizrj9ma666063351).

Пример 1:

```python
chocolate_price = 61
amount_money = 60

if amount_money >= chocolate_price:
  print("Take your chocolate")
else:
  print("You need more money")
```

Теперь немного дополняем первый пример, чтобы показать ученикам, как работает оператор "elif".

Пример 2:

```python
chocolate_price = 61
gum_price = 30
amount_money = 60

if amount_money >= chocolate_price:
  print("Take your chocolate")
elif amount_monemy >= gum_price:
  print("Take your gum!")
else:
  print("You need more money")
```

## 5. Функции

>[!TIP]
>В Python, функция — это именованная последовательность инструкций, предназначенная для выполнения конкретной задачи. Она представляет собой подпрограмму, которая может принимать аргументы (параметры), выполнять операции над ними и возвращать результат (значение). Функции являются важным инструментом для организации, структурирования и повторного использования кода в Pytho

Пример 1:

```python
num_1 = 5
num_2 = 8

def sum():
  print(num_1 + num_2)

sum()
```

Дополним пример из функции выше добавим к ней еще функционала

Пример 2:

```python
def sum(num_1, num_2):
  print(num_1 + num_2)

sum(2, 3)
```

В качестве завершающего этапа урока, в зависимости от оставшегося времени, можно предложить ученикам самостоятельно решить задачи для практики или вместе разобрать дополнительные примеры для более глубокого усвоения материала.

Уровень 1: “Проверка возраста”

Условие:

Напишите программу, которая запрашивает у пользователя его возраст (целое число). Если возраст больше или равен 18, выведите сообщение “Вы совершеннолетний”. Иначе, выведите сообщение “Вы несовершеннолетний”.

Решение:

```python
age = int(input("Введите ваш возраст: "))

if age >= 18:
  print("Вы совершеннолетний")
else:
  print("Вы несовершеннолетний")
```

Уровень 2: “Большеe из двух чисел”

Условие:

Напишите программу, которая запрашивает у пользователя два числа. Найдите и выведите большее из этих двух чисел. Если числа равны, выведите сообщение “Числа равны”.

Решение:
```python
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 > num2:
  print("Большее число:", num1)
elif num2 > num1:
  print("Большее число:", num2)
else:
  print("Числа равны")
```

Уровень 3: “Калькулятор скидки”

Условие:

Напишите программу, которая запрашивает у пользователя сумму покупки. Если сумма покупки больше 1000, дайте скидку 10%. Выведите итоговую сумму к оплате с учетом скидки (или без нее, если скидка не полагается).

Решение:

```python
purchase_amount = float(input("Введите сумму покупки: "))

if purchase_amount > 1000:
  discount = purchase_amount * 0.10
  final_amount = purchase_amount - discount
  print("Сумма к оплате с учетом скидки:", final_amount)
else:
  print("Сумма к оплате:", purchase_amount)
```

Уровень 4: “Определение времени года”

Условие:

Напишите программу, которая запрашивает у пользователя номер месяца (от 1 до 12). В зависимости от номера месяца, выведите соответствующее время года (“Зима”, “Весна”, “Лето”, “Осень”). Учтите, что декабрь, январь и февраль - это зима, март, апрель и май - весна и т.д.

Решение:

```python
month = int(input("Введите номер месяца (1-12): "))

if month in [12, 1, 2]:
  print("Зима")
elif month in [3, 4, 5]:
  print("Весна")
elif month in [6, 7, 8]:
  print("Лето")
elif month in [9, 10, 11]:
  print("Осень")
else:
  print("Некорректный номер месяца")
```

Уровень 5: “Проверка делимости”

Условие:

Напишите программу, которая запрашивает у пользователя два целых числа. Проверьте, делится ли первое число на второе без остатка. Выведите соответствующее сообщение.

Решение:

```python
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num2 == 0:
  print("На ноль делить нельзя!")
elif num1 % num2 == 0:
  print(num1, "делится на", num2, "без остатка")
else:
  print(num1, "не делится на", num2, "без остатка")
```

Эти задачи позволяют закрепить знания об условных операторах и переменных в Python.
