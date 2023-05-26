# SushiDrop

SushiDrop - это веб-приложение, которое предоставляет пользователям возможность заказывать роллы и суши с доставкой на дом.

## Особенности платформы
1. Каталог продуктов
Пользователи могут просматривать различные блюда, доступные для заказа, с ценами и описаниями. Возможно добавление фотографии блюд для лучшей визуализации.

2. Корзина
После выбора блюд пользователи могут добавлять их в корзину. Корзина позволяет пользователям просмотреть свой заказ, редактировать его и удалять товары, которые им больше не нужны.

3. Оформление заказа
Пользователи могут ввести свои контактные данные, выбрать способ доставки и оплаты

4. Оплата онлайн
Пользователи могут оплатить свой заказ онлайн с помощью различных платежных систем.

5. Отслеживание статуса заказа
Пользователи могут отслеживать статус своего заказа на сайте и получать уведомления о его изменении.

6. Система лояльности
Магазин может предоставлять систему лояльности для постоянных клиентов, таких как скидки и бонусы.

7. Рейтинг продуктов
Пользователи могут оставлять отзывы и рейтинг продуктов, что поможет другим пользователям выбрать лучшее блюдо.

8. Определение местоположения
Пользователи могут ввести свой адрес и определить свое местоположение на карте для быстрой и точной доставки.

9. Адаптивный дизайн
Сайт может иметь адаптивный дизайн, который обеспечивает корректное отображение на всех устройствах, включая смартфоны и планшеты.

10. Отзывы и рейтинги продуктов
Покупатели могут оставлять отзывы и оценки продуктов, что помогает другим пользователям выбрать лучшие блюда.

11. Различные способы доставки
Пользователи могут выбрать различные способы доставки, например, доставку на дом или самовывоз из магазина.

12. Система уведомлений
Пользователи могут получать уведомления о статусе своего заказа, изменениях в меню и специальных предложениях.

13. Аналитика продаж
Магазин может предоставлять отчеты и аналитику по продажам, что поможет управлять бизнесом более эффективно.


## Цель
Предоставить удобный и быстрый способ заказа и доставки японской кухни для широкой аудитории клиентов.
Главной целью является удовлетворение потребностей клиентов и обеспечение ими высокого уровня сервиса, что способствует удержанию клиентов и привлечению новых. 
Другие цели могут включать увеличение доходов, увеличение узнаваемости бренда, расширение ассортимента продуктов и улучшение качества продукции и услуг.

## Какие проблемы решает платформа
1. Необходимость посещения магазина
Клиенты больше не должны лично посещать магазин, чтобы заказать роллы или суши.

2. Очереди и задержки
Пользователи могут избежать длительных очередей и задержек, связанных с заказом еды в магазине.

3. Недоступность
Клиенты могут заказать еду в любое время, даже когда магазин закрыт.

4. Ограниченный выбор
Пользователи могут иметь больший выбор блюд и опций на сайте магазина, чем в физическом магазине.

5. Удобство заказа
Клиенты могут заказать блюда онлайн, не выходя из дома или офиса, что экономит время и упрощает процесс заказа.

## Запуск приложения

### Предварительные требования

* Python (3.7+)
* Node.js (+14.x)
* Redis

### Django + Celery

1. Клонируем репозиторий
2. Создаем виртуальное окружение и активируем его

 - `python -m venv env`
 - `source env/bin/activate`

3. Установка зависимостей Pethon

 - `pip install -r requirements.txt`

4. Запускаем Redis

- `redis-server`

5. Применяем миграции

 - `python3 manage.py migrate`

6. Запускаем сервер Django

 - `python3 manage.py runserver`

7. В новом терминале с активированным виртуальным окружением запускаем Celery

- `celery -A sushidrop worker -l info`

### Vue.js

1. Переходим в папку frontend

 - `cd frontend`

2. Устанавливаем зависимости Node.js

 - `npm install`

3. Запускаем сервер Vue.js

 - `npm run serve`

## Использование

Переходим по адресу `http://localhost:8080`
