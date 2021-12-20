from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LaptopView(LoginRequiredMixin,View):
    def get(self,req):
        form = LaptopModelForm()
        context = {'form':form}
        return render(req,'app1/add_laptop.html',context)

    def post(self,req):
        form =LaptopModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('lap_show')

class ListView(View):
    def get(self,req):
        lap_object = Laptop.objects.all()
        context = {'lap_object':lap_object}
        return render(req,'app1/show_laptop.html',context)

class UpdateView(LoginRequiredMixin,View):
    def get(self,req,i):
        lap=Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=lap)
        context = {'form':form}
        return render(req,'app1/add_laptop.html',context)

    def post(self,req,i):
        lap = Laptop.objects.get(id=i)
        form =LaptopModelForm(req.POST,instance=lap)
        if form.is_valid():
            form.save()
            return redirect('lap_show')

class DeleteView(LoginRequiredMixin,View):
    def get(self,req,i):
        lap = Laptop.objects.get(id=i)
        lap.delete()
        return redirect('lap_show')

