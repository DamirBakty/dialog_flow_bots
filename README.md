# БОТЫ на VK и Telegram с связанные с DialogFlow от Google

Боты умеют отвечать на заготовленные фразы и вопросы из DialogFlow. Можете создать проект и тренировать по [ссылке](https://cloud.google.com/dialogflow/es/docs/quick/setup).

Как работает в Telegram:


![tg](https://github.com/DamirBakty/dialog_flow_bots/assets/79716704/cf272c28-5241-46fb-b0ae-e4ca4fb7ab46)




Как работает в VK:

![vk](https://github.com/DamirBakty/dialog_flow_bots/assets/79716704/38b46c22-3eb0-476f-b668-d89b19830aeb)



## Как запустить

* Скачайте код
* Перейдите в корневую папку проекта
* Создайте виртуальное окружение
* Установите зависимости

```bash
$ pip install -r requirements.txt
```





PATH_TO_QUESTIONS=
* Создайте .env файл и скопируйте содержимое из .env.example
* Поменяйте данные под свой проект
* * TG_BOT_TOKEN - Токен телеграм бота
* * DIALOGFLOW_API_KEY - API ключ от проекта DialogFlow
* * DIALOGFLOW_PROJECT_ID - ID проекта DialogFlow
* * PATH_TO_CREDENTIALS - Путь где лежит данные для авторизации по API. Скачайте данные для авторизации по API в формате JSON. Можете включить API и скачать по этой [ссылке](https://cloud.google.com/docs/authentication/api-keys)
* * VK_BOT_TOKEN - API Ключ от бота сообщества в VK.
* * PATH_TO_QUESTIONS - Путь где лежит заготовленные фразы и ответы для DialogFlow. Пример по [ссылке](https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json)


* Запустите бота для Telegram
```bash
$ python tg_bot_start.py
```

* Запустите бота для VK
```bash
$ python vk_bot_start.py
```
