from django.contrib import admin
from apps.profiles_api import models

admin.site.register(models.UserProfile)