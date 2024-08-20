from django.contrib import admin
from .models import ChatGroup, GroupMessage
# Register our models here.
admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
