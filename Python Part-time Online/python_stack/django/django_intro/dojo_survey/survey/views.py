from django.shortcuts import render, HttpResponse

def survey(request):
    return render(request, "survey.html")

def result(request):
    if request.method == "POST":
        test = {
            "firstName" : request.POST["firstName"]
            "lastName" : request.POST["lastName"]
        }
        return render(request, "result.html", test)