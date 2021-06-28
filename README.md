# Тестовое задание, которое было создано по требованиям, которые описаны ниже.
*Чтобы запустить проекта на своем ПК можно использовать docker. Для этого нужно клонировать git репозиторий и вызвать команду docker-compose up*

## Заметки

- В проекте для ознокомительных целей исспользовалось расширение Flask-RESTX. Необходимости в его использовании не было, все то же самое с небольшими изменениями в коде можно написать без этого расширения
- Если необходимо, готов написать тесты. На данный момент их нет

## Требования

*Необходимо используя python3.6+ реализовать RESTful-сервис на Flask/Django/Tornado, со следующими методами:*

### Блок авторизации

1. /login?phone=<телефон> GET запрос с номером телефона, в ответ должен прийти 6-значный код
2.  /login POST запрос вида *`{"phone": "[+71111111111](tel:+71111111111)", "code": "QWDCR4"}`* - в ответ должен прийти `{"status": "OK"}` если код верный и `{"status": "Fail"}` если код не верный. 
Можно хранить коды для авторизации в коде, не используя базу данных или кэш хранилища для этого

### Блок работы с ссылками

1.  /structure GET запрос, В ответ должен прийти словарь с количеством каждого типа HTML-тэгов (например *`{"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}`*) для сайта [freestylo.ru](http://freestylo.ru/)
2. /structure?link=<ссылка> То же, что и выше, но теперь сайт задается в запросе
3. /structure?link=<ссылка>&tags=html,img То же что и выше, но теперь помимо ссылки задается массив тэгов через запятую, которые нужно вернуть в ответе
4. /check_structure POST запрос вида  `{"link": "freestylo.ru", "structure": {"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}}` 
Который для данный ссылки проверяет структуру html тэгов. В ответ должно приходить `{"is_correct": True}` если все верно и `{"is_correct": False, "difference": {"p": 2, "img": 1}}`  если есть ошибки, где difference - это разница структур. 
Например, если верная структура - `{"html": 1, "head": 1, "body": 1, "p": 4}` а передавалась структура `{"html": 1, "head": 1, "body": 1, "p": 2, "img": 1}` то разница будет `{"p": 2, "img": 1}`

### Что приветствуется(но не обязательно)

- [x] Валидация входящих данных
- [x] Корректная обработка ошибок(если они будут, то нужно каким-либо образом донести эти ошибки до пользователяпользователя)
- [ ] Асинхронные запросы
- [ ] Применения кэша там где он применим
- [ ] Написание тестов(любая библиотека, предпочтительнее pytest)
- [x] Оформление проекта с requirements.txt и файлами readme и .gitignore
- [x] Написание корректного Dockerfile для проекта
