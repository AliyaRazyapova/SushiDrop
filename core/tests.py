import os
import django
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sushidrop.settings')
# Загрузите настройки Django
django.setup()

# Теперь вы можете использовать check_password
password = '1'
hashed_password = make_password(password)
print(hashed_password)

is_password_valid = check_password(password, hashed_password)
if is_password_valid:
    print('Пароль верный')
else:
    print('Пароль неверный')
