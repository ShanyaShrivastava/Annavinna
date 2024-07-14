from django.contrib import admin
from .models import *
from .models import User

admin.site.register(foodmart)
admin.site.register(User)