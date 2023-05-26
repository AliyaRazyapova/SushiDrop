from celery import Celery
from django.core.mail import send_mail

app = Celery('sushidrop', broker='redis://localhost:6379/0')


@app.task
def send_password_reset_email(email, reset_token):
    subject = 'Сброс пароля'
    message = f'Для сброса пароля перейдите по ссылке: {reset_token}'
    sender_email = '2458750@gmail.com'
    recipient_email = email

    send_mail(subject, message, sender_email, [recipient_email])
