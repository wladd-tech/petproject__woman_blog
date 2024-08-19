<h1 align="center">Мини-блог про знаменитых женщин</h1>

![demo-gif.gif](https://github.com/wladd-tech/petproject__woman_blog/blob/dev/demo-gif.gif)

## Используемые технологии:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## Установка и использование

### Клонирование из репозитория GitHub

Чтобы начать работу с веб-приложением petproject\_\_woman_blog, вы можете клонировать репозиторий с GitHub, выполнив следующие действия:

1. **Клонирование из репозитория**:

   ```bash
   git clone https://github.com/wladd-tech/petproject__woman_blog.git

   ```

2. Перейдите в папку проекта:
   ```bash
   cd sitewomen

   ```
3. Создайте и активируйте виртуальное окружение python (необязательно, но рекомендуется):

   ```bash
   py -m venv myworld
   myworld\Scripts\activate.bat

   ```

4. Установка зависимостей проекта:
   ```bash
   pip install -r requirements.txt

   ```
5. Создайте env-файл в корневом каталоге вашего проекта:

   ```bash
   .env.defaut переименуйте в .env

   ```

6. Устновите необходимые настройки в .env исходя из ваших данных

7. Выполните миграции базы данных:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

   ```
8. Создайте учетную запись суперпользователя (для доступа администратора)
   ```bash
   python manage.py createsuperuser

   ```
9. Запустите сервер разработки:
   ```bash
   python manage.py runserver

   ```
10. Откройте свой веб-браузер и перейдите по ссылке http://localhost:8000 чтобы получить доступ к веб-приложению.
