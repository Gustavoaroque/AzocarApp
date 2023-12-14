from rest_framework import serializers
from Bodega.models import GeneralArticle, DetailArticle, Loan,Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta: 
        model =  Category
        fields = '__all__'

class GeneralArticleSerializers(serializers.ModelSerializer):
    class Meta: 
        model =  GeneralArticle
        fields = '__all__'

class DetailArticleSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  DetailArticle
        fields = '__all__'

class LoanSerializers(serializers.ModelSerializer):
    class Meta: 
        model =  Loan
        fields = '__all__'
        