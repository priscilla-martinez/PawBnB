from django.contrib import admin
from .models.user import User
from .models.home import Home

# Register your models here.
admin.site.register(User)
admin.site.register(Home)