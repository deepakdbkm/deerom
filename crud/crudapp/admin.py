from django.contrib import admin

# Register your models here.
from crudapp.models import task

admin.site.register(task)