# Register your models here.
from django.contrib import admin
from .models import Post,Answers

admin.site.register(Post)
admin.site.register(Answers)
