from django.db import  models

class Product(models.Model):
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 500)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/files' , null=True , blank=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails')
    link = models.CharField(null=True , blank= True , max_length= 200)
    fileSize = models.CharField(null=True , max_length= 10)


    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product , default= None , on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='uploads/imagee' , blank=True)