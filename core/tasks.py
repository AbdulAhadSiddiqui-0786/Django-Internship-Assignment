from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    try:
        send_mail(
            subject='Welcome!',
            message='Thanks for registering.',
            from_email='settings.EMAIL_HOST_USER',
            recipient_list=[user_email],
        )
        print(f"[✔] Email sent to {user_email}")
    except Exception as e:
        print(f"[❌] Failed to send email to {user_email}: {e}")
