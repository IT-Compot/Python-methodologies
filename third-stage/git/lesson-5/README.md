Продолжаем работать над проектом анализатор эмоциональной окраски текста

Заходим в GitHub Desktop и IDE

Теперь попробуем воспользоваться не моделью Russian, а другой молью, чтобы улучшить обработку текста.

В терминале пишем команду:

```
python -m spacy download ru_core_news_md
```

Теперь поработаем над лемматизацией текста

Лемматизация текста — это процесс приведения слова к его словарной форме (лемме). Представьте, что у вас есть разные формы слова, например: “бежал”, “бежит”, “бегущие”. Лемматизация преобразует все эти формы к одной, базовой форме – “бежать”.

Простыми словами: Лемматизация - это как если бы вы разбирали слово по частям и оставляли только его основу, чтобы понимать, что это за слово.

Дополняем код новой моделью. Новые строке отметил в конце `*`.

``` python
from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md #* 1

#model = Russian()
model = ru_core_news_md.load() #* 2

text = model("Фильм очень понравился, хороший сюжет, классные актеры, но концовка чуть испортила впечатление, а так твёрдая 8")

text_list = [i for i in text]
print(text_list)

filter_text_list = [i for i in text_list if not i in STOP_WORDS]

lemma_text = [i.lemma_ for i in text] #* 3
print(lemma_text) #* 4
```

После того, как протестировали код выше. Пробуем теперь одновременно приенить и лемму, и фильтр, который мы использовали на прошлом уроке.

``` python
from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md

#model = Russian()
model = ru_core_news_md.load()

text = model("Фильм очень понравился, хороший сюжет, классные актеры, но концовка чуть испортила впечатление, а так твёрдая 8")

lemma_text = [i.lemma_ for i in text] #*

filter_text_list = [i for i in lemma_text if not i in STOP_WORDS] #*
print(filter_text_list)
```

Теперь проверяем, что наши изменения отобразились в GitHub Desktop. Коммитим, пушим.

2. Переходим к нахождению положительных и отрицательных слов

Устанавливаем пакет textblob версии 0.18.0.post0.

Дополняем наш код новым функционалом.

``` python
from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
from textblob import TextBlob #*
import ru_core_news_md

#model = Russian()
model = ru_core_news_md.load()

text = model("Фильм очень понравился, хороший сюжет, классные актеры, но концовка чуть испортила впечатление, а так твёрдая 8")

lemma_text = [i.lemma_ for i in text]
filter_text_list = [i for i in lemma_text if not i in STOP_WORDS]

analysis = TextBlob(str(filter_text_list)) #*
sentiment = analysis.sentiment.polarity #*

if sentiment > 0: #*
	print("Positive") #*
elif sentiment < 0: #*
	print("Negative") #*
else: #*
	print("Neutral") #*
```

Тестим код выше, а именно в `text = model("...")` пишем разные вариации комментариев, чтобы проверить правильно ли наша программа анализирует отзыв.

В итоге, мы видим, что нет. Т.к. на данный момент пакет `textblob` умеет работать только с английским языком.

3. Добавляем работу с пакетом translate

Устанавливаем пакет `translate` версии 3.6.1 и дополняем наш код новым функционалом.

``` python
from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
from textblob import TextBlob
from translate import Translator #*
import ru_core_news_md

#model = Russian()
model = ru_core_news_md.load()

text = model("Фильм очень понравился, хороший сюжет, классные актеры, но концовка чуть испортила впечатление, а так твёрдая 8")

lemma_text = [i.lemma_ for i in text]
filter_text_list = [i for i in lemma_text if not i in STOP_WORDS]

translator = Translator(from_lang="Russian", to_lang="English") #*
translated_text = translator.translate(str(filter_text_list)) #*

analysis = TextBlob(translated_text) #*
sentiment = analysis.sentiment.polarity

if sentiment > 0:
	print("Positive")
elif sentiment < 0:
	print("Negative")
else:
	print("Neutral")
```

Тестим код выше, а именно в `text = model("...")` пишем разные вариации комментариев, чтобы проверить правильно ли наша программа анализирует отзыв.

Делаем новый коммит пишем в нём, что у нас "finish version 1.0", пушим.


4. Добавляем изменения другого участника с GitHub

Заходим в GitHub в наш репозиторий и добавляем новый файл.

![alt text](images/1.png)

Делаем его текстовым, пишем туда комментарии и жмем "commit changes...".

![alt text](images/2.png)

Возвращаемся на GitHub Desktop делаем "Fetch origin" и "Pull origin". Не забываем с ребятами проговаривать, что делает каждая из команд.

Проверяем в IDE, что новый файл появился.

5. Самостоятельная работа

Даем ученика самостоятельную задачу, чтобы они сами попробовали воспользоваться данными из файла (прочитать их и проанализировать с помощью нашей программы), но перед этим создаем новую ветку.

![alt text](images/3.png)
