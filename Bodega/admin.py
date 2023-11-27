from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(GeneralArticle)
admin.site.register(DetailArticle)
admin.site.register(Loan)