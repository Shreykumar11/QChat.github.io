from django.contrib import admin
from .models import UserProfile, chatMessages


admin.site.register(UserProfile)
admin.site.register(chatMessages)

