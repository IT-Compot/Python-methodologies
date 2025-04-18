Устанавливаем библиотеки pip install -r requirements.txt

Делаем изменения в you-get(файлик), сохраняем и заходим в git hub desktop, чтобы увидеть изменения

Создаем fork (ноходится рядом с commit) и сохраняем изменения на нашем репозитории, после делаем commit

>[!TIP]
>**Форк в Git** — это личная копия чужого репозитория, которая хранится в учётной записи на GitHub.
>
>Форк репозитория позволяет свободно экспериментировать с изменениями, не затрагивая исходный проект. Это особенно полезно для участия в проектах с открытым исходным кодом.
>
>**Некоторые особенности форка**:
>
>* **Независимая копия**. Изменения, внесённые в форк, не влияют на оригинал.
>
>* **Вклад**. Можно изменить свой форк, а затем создать запрос на извлечение, чтобы предложить изменения в исходном репозитории.
>
>* **Совместная работа**. Форки полезны для совместной разработки, когда несколько участников могут работать над своими версиями и вносить изменения в исходный проект с помощью запросов на извлечение.

Показываем вкладку история

Используем свреху команду push origin

>[!TIP]
>push origin — это команда, которая позволяет отправлять локальную ветку на удалённый репозиторий.

git push: Это команда Git, которая отправляет (загружает) локальные коммиты в удаленный репозиторий. По сути, вы говорите: “Git, возьми мои локальные изменения и отправь их на сервер”.

origin: Это псевдоним (alias) для URL-адреса вашего удаленного репозитория. По умолчанию, когда вы клонируете репозиторий с GitHub, origin автоматически настраивается как URL-адрес этого репозитория на GitHub. Думайте об origin как о сокращенном имени для удаленного репозитория.

Заходим на git hub

Ищем наш репозитоий

![alt text](images/1.png)

Показываем где мы сделали коммиты

![alt text](images/2.png)

Изменяем любой файлик в репозитории, чтобы потом стянуть себе изменения

Заходим в git hub deskop и жмем fetch origin, чтобы получить изменения сделанные на удаленным репозитории

git fetch origin — это команда в распределённой системе контроля версий Git, которая используется для обновления локального репозитория с изменениями из удалённого репозитория.

Она загружает коммиты, файлы и ссылки из удалённого репозитория без слияния их с текущей веткой.

А потом используем pull origin

Pull origin в контексте GitHub — это команда, которая загружает изменения из удалённого репозитория (origin) в локальный репозиторий (main).

Она не только загружает последние изменения, но и автоматически сливает их с текущей локальной веткой

Потом заходим в pycharm и проверяем изменения


## Разбираемся с ветками

![alt text](images/3.png)

Создаем новую ветку

![alt text](images/4.png)

И сделать publish branch

Смотрим на github, что данная ветка появилась

Попробуем изменить данную ветку (удаляем почти все с нее) (Изменяем на github desktop_

Делаем commit

И пушим (кнопка сверху)

Заходим на github и наблюдаем за нашей созданной веткой

Теперь попробуем внести изменения в ветку develop для это в pycharm создадим новый файлик с кодом

Коммитим, пушим, заходим в git hub и смотрим за изменениями в нашей ветке test

Пробуем объединить наши ветки 

В git hum заходим в pull requests

Выбираем с каким репозиторием будем сливать (ваше имя git) и кого (ветка test)

![alt text](images/5.png)

Создаем pull requets и делаем mergre

После видим, что всё с ветки develop удалилось. Т.к. когда мы делали ветку test, то наши изменения, а именно удаления тоже запомнились и поэтому они применились к ветке develop.

На след уроке посмотрим, как откатывать изменния
