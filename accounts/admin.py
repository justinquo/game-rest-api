from django.contrib import admin
from .models import User

from .models import *


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User


admin.site.register(User, UserAdmin)
