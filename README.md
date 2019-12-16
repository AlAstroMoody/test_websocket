**Как передать данные из БД по вебсокету? При запуске отдельного сервера с ним, он не видит файлы джанго **
Запуск сервера с вебсокетом: 
    python3 my_server.py
Запуск сервера джанго: 
    python3 manage.py runserver


Тестовое задание:
1. Создать Django приложение в котором можно добавлять URL’s в административном
разделе (/admin/). С возможностью указать сдвиг во времени (минуты, секунды) через
сколько какой URL когда будет обработан (timeshift).
• Frontend
• Сделать два окна textarea.
• В первое окно выводить информацию об успехе или ошибке обработки URL’a (для
backend можно воспользоваться очередями Queue).
• Во второе вывести данные полученные из пункта 2.
2. Создать сервер для парсинга сайтов по URL’ам указанным в базе Django приложения
(п. 1), в указанный сдвиг времени или сразу запускать если не указан сдвиг.
• На сайтах получить
• Заголовок (title)
• Определить кодировку страницы
• Если есть, найти и получить H1
• Вывести данные во второе окно.
Основные моменты:
I. Сервер для обработки URL может быть выполнен в виде команды, либо в виде
полноценного сервера с собственными процессами/нитями (process/thread).

II. Данные по обработанным URL’ам сохранять в базу и при перезагрузке выводить их во
втором textarea.

III. Все сообщения в первом окне должны начинаться с даты и двоеточия
“<дата dd.mm.yyyy HH:mm:ss>: ”.

IV. Все сообщения во втором окне начинаются с URL и тире (dash), вида “http://example.com —”, с последующим перечислением что получено и чего нет. Если получить ничего не
удалось - тогда просто URL.

V. Запрещается использовать любые брокеры сообщений которым нужны собственные
серверные платформы (RabbitMQ, ActiveMQ и т.д.)

VI. Рабочий сайт должен запускаться из командной строки одной командой, вида “python
manage.py runserver” или “python run.py” или “python -m module -c command”, либо
bash/sh скриптом.

VII. Все зависимости должны устанавливаться из файла “requirements.txt”, который будет
лежать в корне кодового репозитория (зависимости которых нет в Pypi, указывать в
“http[s]://“ формате).

VIII. Описать процесс запуска кода на локальной машине

IX. Код должен запустится и работать на машине на которой установлен только python и
сопутствующие библиотеки, SQLite.
Плюсом рассматривается:
- использование базовых модулей Python (из комплекта поставки)
- использование на frontend’e Websockets.
- Обвязка (wrapping) стандартного Django WSGI Сервера методами кот. могут в
мультипроцессорном потоке запускать процессы по обработке URL’s (не обязательно).
- Мульти-версионный и переносимый код (Python 2.5,2.6,2.7,3.2,3.3,3.4).
Репозитарий опубликовать в любом доступном месте (GIT, Mercurial, Bazaar etc.) как
публичный.
github.com, gitlab.com, bitbucket.org, Sourceforge (sf.net), launchpad.net
