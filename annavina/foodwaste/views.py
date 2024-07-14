from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from geopy.distance import great_circle
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate
from .models import foodmart
from geopy.geocoders import Nominatim
from .forms import SearchFoodMartForm,FoodmartForm
import geopy.distance

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')


def api(request):
    form = SearchFoodMartForm(request.GET or None)
    if form.is_valid():
        pincode = form.cleaned_data['pincode']
        max_distance = form.cleaned_data['distance']
        geolocator = geopy.Nominatim(user_agent="foodwaste")
        location = geolocator.geocode(pincode)
        user_lat = location.latitude
        user_long = location.longitude
        nearest_foodmart = None
        min_distance = float('inf')

        for foodMart in foodmart.objects.all():
            first = (user_lat, user_long)
            second = (foodMart.lat, foodMart.lon)
            distance = geopy.distance.great_circle(first, second).miles

            if distance <= max_distance and distance < min_distance:
                min_distance = distance
                nearest_foodmart = foodMart

        if nearest_foodmart:
            context = {
                'nearest_foodmart': nearest_foodmart,
                'distance': min_distance,
            }
            return render(request, 'nearest_foodmart.html', context)
        else:
            return render(request, 'no_result_found.html')
    else:
        return render(request, 'search_form.html', {'form': form})


def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('foodmart_add')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('api')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def foodmart_list(request):
    foodmarts = foodmart.objects.all()
    return render(request, 'foodmart_list.html', {'foodmarts': foodmarts})


def foodmart_add(request):
    if request.method == 'POST':
        form = FoodmartForm(request.POST)
        if form.is_valid():
            foodmart_instance = form.save(commit=False)
            foodmart_instance.save()
            return redirect('foodmart_list')
    else:
        form = FoodmartForm()
        return render(request, 'foodmart_form.html', {'form': form})

def foodmart_edit(request, pk):
    foodmart_instance = foodmart.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FoodmartForm(request.POST, instance=foodmart_instance)
        if form.is_valid():
            foodmart_instance = form.save(commit=False)
            foodmart_instance.save()
            return redirect('foodmart_list')
    else:
        form = FoodmartForm(instance=foodmart_instance)
    
    return render(request, 'foodmart_form.html', {'form': form})


def map(request):
    foodmarts = foodmart.objects.all()
    return render(request,'map.html',{'foodmarts' : foodmarts})

def about(request):
    return render(request,'about.html')