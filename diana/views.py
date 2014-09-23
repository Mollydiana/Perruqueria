from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from diana.forms import ProfileUserCreationForm
from perruqueria import settings




def home(request):
    # if request.user.is_authenticated():
    #     return redirect('home')
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
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

#
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return redirect('home')
#         else:
#             pass
#     else:
#         pass



# def login(request):
#     state = "Please log in below..."
#     first_name = ''
#     last_name = ''
#     password = ''
#
#     if request.POST:
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']
#
#         user = authenticate(first_name=first_name, last_name=last_name, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#
#                 return HttpResponseRedirect('home')
#             else:
#                 state = "Your account is not active, please contact the site admin."
#         else:
#             state = "Your username and/or password were incorrect."
#
#     return render_to_response(
#         'registration/login.html',
#         {
#         'state':state,
#         'first_name': first_name,
#         'last_name': last_name,
#         'password': password,
#
#         },
#         context_instance=RequestContext(request)
#     )