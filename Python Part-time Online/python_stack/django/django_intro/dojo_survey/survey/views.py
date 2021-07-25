from django.shortcuts import render, HttpResponse

def survey(request):
    return render(request, "survey.html")

def result(request):
    if request.method == 'POST':
        context = {
            'firstName': request.POST['firstName'],
            'lastName': request.POST['lastName'],
            'country': request.POST['country'],
            'dojoLocation': request.POST['dojoLocation'],
            'comment': request.POST['comment'],
        }
        print(request.POST)
        return render(request, 'result.html', context)
    return render(request, 'result.html')