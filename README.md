# БОТЫ на VK и Telegram с связанные с DialogFlow от Google

Боты умеют отвечать на заготовленные фразы и вопросы из DialogFlow. Можете создать проект и тренировать по [ссылке](https://cloud.google.com/dialogflow/es/docs/quick/setup).

## Как запустить

* Скачайте код
* Перейдите в корневую папку проекта
* Создайте виртуальное окружение
* Установите зависимости

```bash
$ pip install -r requirements.txt
```

VK_BOT_TOKEN=
PATH_TO_QUESTIONS=
* Создайте .env файл и скопируйте содержимое из .env.example
* Поменяйте данные под свой проект
* * TG_BOT_TOKEN - Токен телеграм бота
* * DIALOGFLOW_API_KEY - API ключ от проекта DialogFlow
* * DIALOGFLOW_PROJECT_ID - ID проекта DialogFlow
* * PATH_TO_CREDENTIALS - Путь где лежит данные для авторизации по API. Скачайте данные для авторизации по API в формате JSON. Можете включить API и скачать по этой [ссылке](https://cloud.google.com/docs/authentication/api-keys)
* * VK_BOT_TOKEN - API Ключ от бота сообщества в VK.
* * PATH_TO_QUESTIONS - Путь где лежит заготовленные фразы и ответы для DialogFlow. Пример по (ссылке)[https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json]


* Запустите бота для Telegram
```bash
$ python tg_bot_start.py
```

* Запустите бота для VK
```bash
$ python vk_bot_start.py
```
