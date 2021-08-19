from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import Registration, RegistrationManager
import bcrypt

def register(request):
    pass
    if request.method == "GET":
        return render (request, 'login_and_regis.html')
    elif request.method == "POST":
        # Validates input data meets standards in models
        errors = Registration.objects.registration_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # Sends data and creates objects is everything is verified
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = Registration.object.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash,
                c_password=request.POST['c_password'],
            )
            # Saves data in sessions for future use.
            request.session['user_id'] = new_user.id
            return redirect('/success')
    else:
        return redirect ('/')

def success(request):
    pass
    # Check request method. Redirects on unapproved reuest method.
    if request.method == "GET":
        context = {
            "user" : request.session['user_id']
        }
        return render(request,'success.html', context)
    return redirect ('/')

def users(request):
    context = {
    "users" : Registration.objects.all(),
    }
    return render(request, 'shows.html', context)

def login(request):
    email = User.object.filter(email=request.POST['email'])
    if email:
        logged_user = email[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['user_id']=logged_user.id
            return redirect('/success')
    errors = Login.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')