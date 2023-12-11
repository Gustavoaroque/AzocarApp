from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET','POST'])
def getAllCategories(request):
    if request.method == 'GET':
        
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        newCatSer = CategorySerializers(data=request.data)
        if newCatSer.is_valid():
            newCatSer.save()
            return Response(newCatSer.data)
        return Response(newCatSer.errors)
        

@api_view(['GET','POST'])
def getAllDetArticles(request):
    if request.method == 'GET':
        detArticles = DetailArticle.objects.all()
        serializer = DetailArticleSerializer(detArticles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        newDetArticle = DetailArticleSerializer(data = request.data)
        if newDetArticle.is_valid():
            newDetArticle.save()
            return Response(newDetArticle.data)
        return Response(newDetArticle.errors)

@api_view(['GET','POST'])
def getAllGenArticles(request):
    if request.method == 'GET':
        genArticles = GeneralArticle.objects.all()
        serializer = GeneralArticleSerializers(genArticles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        newGenArticle = GeneralArticleSerializers(data = request.data)
        if newGenArticle.is_valid():
            newGenArticle.save()
            return Response(newGenArticle.data)
        return Response(newGenArticle.errors)
    
@api_view(['GET','POST'])
def getAllLoans(request):
    if request.method == 'GET':
        loan = Loan.objects.all()
        serializer = LoanSerializers(loan, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        newLoan = LoanSerializers(data = request.data)
        if newLoan.is_valid():
            newLoan.save()
            return Response(newLoan.data)
        return Response(newLoan.errors)

@api_view(['GET'])
def getCategory(request,catid):
    category = Category.objects.get(CatID=catid)
    serializers = CategorySerializers(category, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getGenArticle(request,detartid):
    category = Category.objects.get(CatID=detartid)
    serializers = CategorySerializers(category, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getDetArticle(request,genartid):
    uniqueDetArt = DetailArticle.objects.get(DetailArticle=genartid)
    serializers = CategorySerializers(uniqueDetArt, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getLoan(request,loanid):
    loan = Loan.objects.get(loanID=loanid)
    serializers = LoanSerializers(loan, many=False)
    return Response(serializers.data)


