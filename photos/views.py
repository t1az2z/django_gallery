from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


# Create your views here.
from .models import Photo
from .forms import PostPhoto


def view(request):
    # Функция вывода главной страницы
    queryset = Photo.objects.all()
    context = {
        'photos': queryset,
    }
    return render(request, 'photo.html', context)


def detail(request, id):
    instance = get_object_or_404(Photo, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
        "commentary": instance.commentary
    }
    return render(request, "detail.html", context)


def upload(request):
    form = PostPhoto(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/')
    context = {
        "form": form,
    }
    return render(request, "post_photo.html", context)


# def delete(request):
#     return HttpResponse("<h1>delete in work</h1>")
