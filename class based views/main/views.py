from django.shortcuts import render,redirect
from main.forms import StyleForm
from main.models import Style
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)        

class StyleUpdate(UpdateView):
    model = Style   
    fields = ['text','image'] 
    success_url = '/stylelist/'


class StyleList(ListView):
    model = Style
    template_name = 'main/stylelist.html'  
    context_object_name = 'styles'

class StyleDelete(DeleteView):
    model = Style
    success_url = '/stylelist/'

class StyleDetail(DetailView):
    model = Style
    template_name = 'main/style_detail.html'


class CreateStyle(CreateView):  
    model = Style   
    fields = ['text','image'] 
    success_url = '/stylelist/'
