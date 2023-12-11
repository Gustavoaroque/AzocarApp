from django.urls import path
from . import views
urlpatterns = [
    path('category/',views.getAllCategories),
    path('detarticles/',views.getAllDetArticles),
    path('genarticles/',views.getAllGenArticles),
    path('loan/',views.getAllLoans),

    path('category/<int:catid>', views.getCategory),
    path('detarticle/<int:detartid>', views.getGenArticle),
    path('genarticles/<int:genartid>', views.getDetArticle),
    path('loan/<int:loanid>', views.getLoan)
]