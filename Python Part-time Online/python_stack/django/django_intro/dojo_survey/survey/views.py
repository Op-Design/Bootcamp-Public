from django.shortcuts import redirect, render, HttpResponse

def survey(request):
    return render(request, "survey.html")

def result(request):
    request.session['firstName'] = request.POST['firstName'],
    request.session['lastName'] = request.POST['lastName'],
    request.session['country'] = request.POST['country'],
    request.session['dojoLocation'] = request.POST['dojoLocation'],
    request.session['comment'] = request.POST['comment'],
    return redirect('/session')

def result2(request):
    # IMMEDIATELY BELOW is former code used for request.post ...
    if request.method == 'POST':
        context = {
            'firstName': request.POST['firstName'],
            'lastName': request.POST['lastName'],
            'country': request.POST['country'],
            'dojoLocation': request.POST['dojoLocation'],
            'comment': request.POST['comment']
        }
        print(request.POST)
        return render(request, 'result.html', context)
    return render(request, 'result.html')

def session(request):
    return render(request, 'result.html')
    # return render(request, 'result.html')