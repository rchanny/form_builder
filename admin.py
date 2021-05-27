from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Form)
admin.site.register(Assessment)
admin.site.register(Competency)
admin.site.register(Performance)
admin.site.register(Outcome)