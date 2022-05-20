

## Тестовое задание
Необходимо разработать скрипт на языке Python 3, <br>
который будет выполнять следующие функции:

* Получать данные с документа при помощи Google API, сделанного в
[Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit)
(необходимо копировать в свой Google аккаунт и выдать самому себе права).
 

* Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    * Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    * Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
* Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:

* Упаковка решения в docker контейнер
    
* Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
---

## Структура проекта.

При запуске создается база данных "test" (если такой нет на сервере). Далее каждые
60 секунд вытягиваются все данные из таблицы google sheets, добавляется колонка с ценой в рублях по текущему
курсу и сохраняются в базу данных.<br>
Раз в 24 часа из базы данных выбираются все заказы, проверяется дата, и все просроченные
заказы отправляются на указанный чат id в телеграм.

---

## install.

Добавьте в корень проекта ключ от сервисного аккаунта google api,
назовите фаил - creds.json. <br>
В фаиле .env установите переменне вашего токена вашего телеграм бота
и чат id (id чата, куда бот будет отправлять просроченные заказы).<br>
 В переменной SPREADSHEET_ID можно указать другой фаил с таблицей из которой
вытягиваются данные.

---

## deployment.

### manual.

Запустите локальный сервер postgres 127.0.0.1:5432.<br>

```commandline
$ python -m venv venv
```
```commandline
$ source venv/bin/activate
```
```commandline
$ pip install -r requirements.txt
```
```commandline
python main.py
```
###  docker.
```commandline
$ docker-compose up 
```