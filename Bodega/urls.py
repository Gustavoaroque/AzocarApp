from django.urls import path
from . import views
urlpatterns = [
    path('',views.getAllCategories),
    path('post/',views.getDataPOST)
]