from django.urls import path
from . import views
urlpatterns = [
    #Get all the items
    path('category/',views.getAllCategories),
    path('detail_article/',views.getAllDetArticles),
    path('general_article/',views.getAllGenArticles),
    path('loan/',views.getAllLoans),
    #Create
    path('category/create',views.CreateCategory),
    path('detail_article/create',views.CreateDetailArticle),
    path('general_article/create',views.CreateGeneralArticle),
    path('loan/create',views.CreateLoan),

    #View specific register 
    path('category/<int:catid>', views.getCategory),
    path('detail_article/<int:detail_article_ID>', views.getDetArticle),
    path('general_article/<int:general_article_ID>', views.getGenArticle),
    path('loan/<int:loanid>', views.getLoan),

    #Update register
    path('category/<int:category_ID>/update', views.updateCategory),
    path('general_article/<int:general_article_ID>/update', views.updateGeneralArticle),
    path('detail_article/<int:detail_article_ID>/update', views.updateDetailArticle),
    path('loan/<int:Loan_ID>/update', views.updateLoan)

    #Delete Registers

]