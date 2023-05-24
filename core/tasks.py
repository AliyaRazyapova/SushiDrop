from celery import shared_task

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string


@shared_task
def send_password_reset_email(user_id):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_link = f'http://localhost:8080/reset-password/{uid}/{token}/'
        subject = 'Сброс пароля'
        message = render_to_string('email/reset_password.html', {'reset_link': reset_link})
        send_mail(subject, message, '2458750@gmail.com', [user.email])
    except User.DoesNotExist:
        pass
