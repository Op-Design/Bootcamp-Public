from django.shortcuts import redirect, render, HttpResponse
from .models import Users

# show all of the data from a table
def index(request):
    if request.method == 'POST':
        Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email_address = request.POST['email_address'],
            age = request.POST['age'],
        ),
    context = {
        "all_the_users" : Users.objects.all(),
    }
    return render(request, "survey.html", context)