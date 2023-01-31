from django.shortcuts import render, HttpResponseRedirect
from FirstApp.models import *
from django.views.generic import ListView,CreateView,DetailView

# Create your views here.
class productview(CreateView):
    model = ProductMainModel
    fields = ("Title","Description","price","Size","Quality")
    
class addview(CreateView):
    model = productImageModel
    fields = ('image')
class ProductDetailViews(DetailView):
    model = ProductMainModel
    fields = ("Title", "Description", "price", "Size", "Quality")

from FirstApp.forms import  imageform
def addimage(request):
    form = imageform()
    print('welcome')
    if request.method=='POST':
        form = imageform(request.POST, request.FILES)
        if form.is_valid():
            print('hi')
            user = form.save(commit=True)