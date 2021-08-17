from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import Registration, RegistrationManager
import bcrypt

def register(request):
    pass
    if request.method == "GET":
        return render (request, 'login_and_regis.html')
    elif request.method == "POST":
        errors = Registration.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = Registration.object.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password'],
                c_password=request.POST['c_password'],
            )
            request.session['user_id'] = new_user.id
            return redirect('/success')
    else:
        return redirect ('/')

def success(request):
    pass
    if request.method == "GET":
        context = {
            "user" : request.session['user_id']
        }
        return render(request,'success.html', context)
    else:
        return redirect ('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def users(request):
    context = {
    "users" : Registration.objects.all(),
    }
    return render(request, 'shows.html', context)

