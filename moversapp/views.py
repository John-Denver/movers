from django.shortcuts import render, get_object_or_404, redirect
from . forms import DriverForm, UserForm
from . models import Driver

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'moversapp/home.html', context)


def detail(request, driver_id):
    drivers = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'moversapp/detail.html', {'driver': drivers})


def help(request):
    return render(request, 'moversapp:help.html')


def add_vehicle(request):
    form = DriverForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        driver = form.save(commit=False)
        driver.vehicle = request.FILES['vehicle']
        driver.user = request.user
        driver.save()
        return render(request, 'moversapp/detail.html', {'driver': driver})
    form = DriverForm()
    return render(request, 'moversapp/add_vehicle.html', {'form': form})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['Drivername']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                drivers = Driver.objects.filter(User=request.user)
                return render(request, 'moversapp/home.html', {'drivers': drivers})
                return redirect('moversapp:home')
            return render(request, 'moversapp/register.html', {'form': form})


def login_driver(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('moversapp:home')

    return render(request, 'moversapp/login.html')


def logout_driver(request):
    logout(request)
    return redirect('moversapp:login_driver')





































