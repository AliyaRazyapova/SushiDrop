from celery import Celery
from celery import shared_task

from django.core.mail import send_mail

app = Celery('sushidrop', broker='redis://localhost:6379/0')


@app.task
def send_password_reset_email(email, reset_token):
    subject = 'Сброс пароля'
    message = f'Для сброса пароля перейдите по ссылке: {reset_token}'
    sender_email = '2458750@gmail.com'
    recipient_email = email

    send_mail(subject, message, sender_email, [recipient_email])


@shared_task
def send_discount_emails():
    from core.models import User

    users = User.objects.all()

    for user in users:
        email_subject = 'Скидки сегодня!'
        email_message = 'У нас сегодня особые скидки только для вас. Заходите на наш сайт и смотрите актуальные предложения.'
        send_mail(email_subject, email_message, '2458750@gmail.com', [user.email])
