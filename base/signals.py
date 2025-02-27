from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(user_logged_in)
def sendEmailLogin(sender, request, user, **kwargs):
    print(f"Enviando e-mail para: {user.email}")
    
    subject = "Login realizado com sucesso!"
    message = f"Olá {user.username}, você acabou de ser registrado no desafio técnico da fidelity!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
