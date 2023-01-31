from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
SIZE_CHOICES = (
    ("1","10"),
    ("2","20"),
    ("3","30")
)

Qualit_choices = (
    ("1","high"),
    ("2","Low"),
    ("3","medium")
)
colour_choices = (
    ("1","red"),
    ("2","blue"),
    ("3","green"),
    ("4","black")
)



class ProductMainModel(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.TextField(max_length=150)
    price = models.IntegerField(unique = True)
    Size = models.CharField(max_length=50,
        choices= SIZE_CHOICES,
        default= '1'
    )

    Quality = models.CharField(max_length=50,
        choices= Qualit_choices,
        default="2"
    )

    def __str__(self):
        return self.Title

class ProductcolorModel(models.Model):
    product = models.ForeignKey(ProductMainModel, null=True,on_delete=models.CASCADE)
    Colour = models.CharField(max_length=50,
        choices= colour_choices,
        default= "1"
    )
    def __str__(self):
        return self.Colour

class productImageModel(models.Model):
    product = models.ForeignKey(ProductMainModel,null=True,on_delete=models.CASCADE)
    image = models.FileField(null=True,blank=True,upload_to="images/",validators=[FileExtensionValidator(allowed_extensions= ['jpg','mp4','mp3','pdf','txt'])])
    class Meta:
        def __str__(self):
             return self.image