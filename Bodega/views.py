from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, GeneralArticle, DetailArticle, Loan
from .serializers import CategorySerializers, GeneralArticleSerializers,DetailArticleSerializer,LoanSerializers


#Get Method
@api_view(['GET'])
def getAllCategories(request):

    categories = Category.objects.all()
    serializer = CategorySerializers(categories, many=True)
    return Response(serializer.data)        

@api_view(['GET'])
def getAllDetArticles(request):
    detArticles = DetailArticle.objects.all()
    serializer = DetailArticleSerializer(detArticles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllGenArticles(request):
    genArticles = GeneralArticle.objects.all()
    serializer = GeneralArticleSerializers(genArticles, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getAllLoans(request):
    loan = Loan.objects.all()
    serializer = LoanSerializers(loan, many=True)
    return Response(serializer.data)

#Create 
@api_view(['POST'])
def CreateCategory(request):
    newCategory = CategorySerializers(data = request.data)
    if newCategory.is_valid():
        newCategory.save()
        return Response(newCategory.data)
    return Response(newCategory.errors)

@api_view(['POST'])
def CreateGeneralArticle(request):
    newGeneral_Article = GeneralArticleSerializers(data = request.data)
    if newGeneral_Article.is_valid():
        newGeneral_Article.save()
        return Response(newGeneral_Article.data)
    return Response(newGeneral_Article.errors)

@api_view(['POST'])
def CreateDetailArticle(request):
    newDetail_Article = DetailArticleSerializer(data = request.data)
    if newDetail_Article.is_valid():
        newDetail_Article.save()
        return Response(newDetail_Article.data)
    return Response(newDetail_Article.errors)

@api_view(['POST'])
def CreateLoan(request):
    newLoan = LoanSerializers(data = request.data)
    if newLoan.is_valid():
        newLoan.save()
        return Response(newLoan.data)
    return Response(newLoan.errors)

#Get one item
@api_view(['GET'])
def getCategory(request,catid):
    try:
        category = Category.objects.get(CatID=catid)
    except category.DoesNotExist:
        return Response({'error': 'Item not found'})
    
    serializers = CategorySerializers(category, many=False)

    # category = Category.objects.get(CatID=catid)
    return Response(serializers.data)
    
        
    
@api_view(['GET'])
def getGenArticle(request,general_article_ID):
    try:
        general_article = GeneralArticle.objects.get(GenArticleID=general_article_ID)
    except:
        return Response({'error':'Item Not Found'})
    
    serializers = GeneralArticleSerializers(general_article, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getDetArticle(request,detail_article_ID):
    try:

        uniqueDetArt = DetailArticle.objects.get(DetArticleID=detail_article_ID)
    except:
        return Response({'error':'Not Found'})
    serializers = DetailArticleSerializer(uniqueDetArt, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getLoan(request,loanid):
    try:
        loan = Loan.objects.get(LoanID=loanid)
    except:
        return Response({'error':'Item not Found'})
    serializers = LoanSerializers(loan, many=False)
    return Response(serializers.data)


#Update one reg
@api_view(['PATCH'])
def updateCategory(request,category_ID):
    try:
        category = Category.objects.get(CatID=category_ID)
    except category.DoesNotExist:
        return Response({'error': 'Item not found'})
    serializers = CategorySerializers(category,data=request.data,partial= True)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return  Response(serializers.errors)

@api_view(['PATCH'])
def updateGeneralArticle(request,general_article_ID):
    try:
        general_Article = GeneralArticle.objects.get(GenArticleID=general_article_ID)
    except general_Article.DoesNotExist:
        return Response({'error': 'Item not found'})
    serializers = GeneralArticleSerializers(general_Article,data=request.data,partial= True)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return  Response(serializers.errors)

@api_view(['PATCH'])
def updateDetailArticle(request,detail_article_ID):
    try:
        detail_Article = DetailArticle.objects.get(DetArticleID=detail_article_ID)
    except detail_Article.DoesNotExist:
        return Response({'error': 'Item not found'})
    serializers = DetailArticleSerializer(detail_Article,data=request.data,partial= True)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return  Response(serializers.errors)

@api_view(['PATCH'])
def updateLoan(request,Loan_ID):
    try:
        loan = Loan.objects.get(LoanID=Loan_ID)
    except loan.DoesNotExist:
        return Response({'error': 'Item not found'})
    serializers = LoanSerializers(loan,data=request.data,partial= True)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return  Response(serializers.errors)