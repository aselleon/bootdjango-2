from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm
from django.views.generic import DetailView, UpdateView

# Create your views here.

def course_info(request):
    return render(request, 'shop/course_info.html', {})

def dev_contacts(request):
    address = 'улица Манаса 8, Алматы 050000'
    dev_list = ({'name': 'Assel Orynbassar', 'phone': '+7 (777) 777-77-77', 'email': '28308@iitu.edu.kz', 'hours': '08:00 AM - 6:00 PM'},
                {'name': 'Muratbekuly Beket', 'phone': '+7 (777) 777-77-88', 'email': '27214@iitu.edu.kz', 'hours': '08:00 AM - 6:00 PM'})
    return render(request, 'shop/dev_contacts.html', context={'devs': dev_list, 'address': address})
    #return render(request, 'shop/dev_contacts.html', {})

def team_members(request):
    return render(request, 'shop/team_members.html', {})

def main_page(request):
    catalogue = ({})
    prods = Products.objects.all()
    return render(request, 'shop/index.html', {'products':prods})

def login_page(request):
    return render(request, 'shop/login.html', {})

class ProductsDetailed(DetailView):
    model = Products
    template_name = 'shop/detailed.html'
    context_object_name = 'product'

class ProductsUpdate(UpdateView):
    model = Products
    template_name = 'shop/create.html'
    # fields = ['title', 'prod_decription']
    form_class = ProductsForm

def create_prod(request):
    error = ''
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            error = "something gone wrong..."
    form = ProductsForm()

    data = {
        'form':form,
        'error':error
    }
    return render(request, 'shop/create.html', data)