from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from diana.forms import ProfileUserCreationForm
from perruqueria import settings




def home(request):
    return render(request, 'home.html')


def servicios(request):
    return render(request, 'servicios.html')


def galeria(request):
    return render(request, 'galeria.html')


def register(request):
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Grazas por rexistrar!, {}{}'.format(user.first_name, user.last_name)
            html_content = '<h2>Grazas por rexistrar!</h2>'.format(user.first_name)
            msg = EmailMultiAlternatives("Benvido!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

