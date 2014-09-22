from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from diana.forms import ProfileUserCreationForm
from perruqueria import settings




def home(request):
    return render(request, 'home.html')


def cita(request):
    return render(request, 'pide_cita.html')


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
            text_content = 'Thank you for signing up for our website, {}{}'.format(user.first_name, user.last_name)
            html_content = '<h2>Thanks {}{} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("cita")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

