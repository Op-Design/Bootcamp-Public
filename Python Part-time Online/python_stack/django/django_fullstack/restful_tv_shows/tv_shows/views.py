from django.shortcuts import redirect, render, HttpResponse
from .models import Show

def root(request):
    return redirect('/shows')

def showsnew(request):
    if request.method == 'GET':
        return render(request, 'show_create.html')
    return redirect('/')

def showscreate(request):
    if request.method == 'POST':
        Show.objects.create(
            title= request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],
        )
        return redirect('/shows')
    return render(request, 'show_create.html')
    
def showsid(request, id):
    if request.method == "GET":
        context = {
            "show" : Show.objects.get(id=id),
        }
    return render(request, 'show.html', context)
    
def shows(request):
    context = {
    "all_the_shows" : Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def showsidedit(request, id):
    if request.method == 'GET':
        context = {
            "id" : id,
            "show" : Show.objects.get(id=id),
        }
        return render(request, 'show_update.html', context)
    return redirect(request, f'/shows/{id}/update')

def showsidupdate(request, id):
    if request.method == 'POST':
        update = Show.objects.get(id=id)
        update.title = request.POST['title']
        update.network=request.POST['network']
        update.release_date=request.POST['release_date']
        update.description=request.POST['description']
        update.save()
        return redirect('/shows')
    return redirect('/shows')

def showsiddestroy(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()
    return redirect('/shows')