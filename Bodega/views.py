from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializers


@api_view(['GET'])
def getAllCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializers(categories, many=True)
    return Response(serializer.data)
# Create your views here.

@api_view(['POST'])
def getDataPOST(request):
    postdata = request.data
    print(postdata)
