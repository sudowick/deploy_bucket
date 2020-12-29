from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from .forms import PhotoForm

def home(request):
    return render(request, 'gallery/home.html', {'posts': Photo.objects.all()})

class PostListView(ListView):
    model = Photo
    template_name = 'gallery/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created']

def upload(request):
    if request.method == 'GET':
        return render(request, 'gallery/upload_pic.html', {'form':PhotoForm()})
    else:
        form = PhotoForm(request.POST, request.FILES)     #fills form automatically
        newphoto = form.save(commit = False)
        newphoto.user = request.user
        newphoto.save()
        return HttpResponse('successfully uploaded')


def myposts(request):
    return render(request, 'gallery/myposts.html', {'posts': Photo.objects.all()})
