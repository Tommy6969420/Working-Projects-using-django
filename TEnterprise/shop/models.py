from django.db import models

# Create your models here.
class Tags(models.Model):
    tag_name=models.CharField(max_length=50)
    def __str__(self):
        return self.tag_name
class Product(models.Model):
    CATEGORY_CHOICES=(('WOMEN','WOMEN'),('MEN','MEN'),('UNISEX','UNISEX'),('CHILD',"CHILD"),("NEWBORN",'NEWBORN'))
    product_id = models.AutoField
    product_tags = models.ManyToManyField(Tags,default='')
    product_name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return f'{self.product_name}'
class FlashSale(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    discount=models.IntegerField(default=0)
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField(auto_now_add=False,)
    def __str__(self):
        return self.product.product_name
class HeroItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.product_name
