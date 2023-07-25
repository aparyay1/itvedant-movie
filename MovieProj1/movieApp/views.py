from django.shortcuts import render
from movieApp.models import Movie
from movieApp.form import MovieForm

# Create your views here.
def displayHome(request):
    return render(request,'htmlpages/home.html')
def displayMovie(request):
    movie_list=Movie.objects.all()
    #mydata={'mlist':movie_list}
    #return render(request,'htmlpages/viewmovie.html',mydata)
    #return render(request,'htmlpages/viewmovie.html',context=mydata)
    return render(request,'htmlpages/viewmovie.html',{'mlist':movie_list})
def addMovie(request):
    form=MovieForm()
    if(request.method=='POST'):
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return displayHome(request)
    return render(request,'htmlpages/addmovie.html',{'amovie':form})
