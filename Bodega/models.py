from django.db import models

class Category(models.Model):
    CatID = models.BigAutoField(primary_key=True)
    CatName = models.CharField(max_length=50, blank=False)
    CatDescription = models.TextField(blank=True)

    def __str__(self):
        return str(self.CatName)
    
class GeneralArticle(models.Model):
    GenArticleID = models.BigAutoField(primary_key=True)
    GenArticleCat = models.ForeignKey("Category",on_delete=models.CASCADE)
    GenArticleName = models.CharField(max_length=50, blank=False)
    GenArticleModel = models.CharField(max_length=50)
    GenArticlePartNumber = models.CharField(max_length=75,blank=False)

    def __str__(self):
        return str(self.GenArticleName)
    
class DetailArticle(models.Model):

    statusCondition = [
        ("Buen estado","Buen estado"),
        ("Defectuoso","Defectuoso"),
        ("Defectuoso de Fabrica","Defectuoso de Fabrica")
    ]
    articleState = [
        ("Disponible","Disponible"),
        ("Prestado","Prestado"),
        ("No Disponible","No Disponible")
    ]

    DetArticleID = models.BigAutoField(primary_key=True)
    GeneralArticleID = models.ForeignKey("GeneralArticle",on_delete=models.CASCADE)
    DetArticleSerialNumber = models.CharField(max_length=50,blank=False)
    DetArticleStatusCondition = models.CharField(max_length=25,choices=statusCondition)
    DetArticleState = models.CharField(max_length=15,choices=articleState)
    # DetArticleImage = 
    DetArticleCreated = models.DateField(auto_now_add=True)
    DetArticleUpdated = models.DateField(auto_now=True)
    DetArticleComments = models.TextField(null=True)

    def __str__(self):
        return str(self.DetArticleSerialNumber)

class Loan(models.Model):
    loanStatus = [
        ("Activo","Activo"),
        ("Terminado","Terminado")
    ]
    LoanID = models.BigAutoField(primary_key=True)
    # LoanUser =
    LoanDetArticle = models.OneToOneField("DetailArticle",on_delete=models.CASCADE)
    LoanStatus = models.CharField(max_length=20,choices=loanStatus)
    LoanDescription = models.TextField()
    LoanDateIn = models.DateField(auto_now_add=True)
    LoanDateOut = models.DateField(blank=True, null = True)

    def __str__(self):
        return str(self.LoanID) 


