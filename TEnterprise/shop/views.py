from django.shortcuts import render
from.models import Product,FlashSale,HeroItem
# Create your views here.
def index(request):
    products=Product.objects.all()
    flashsale=FlashSale.objects.all()
    categories=Product.objects.order_by().values('category').distinct()
    heroitem=HeroItem.objects.all()
    print(categories)
    context={'products':products,'flashsale':flashsale,'categories':categories,'heroitem':heroitem}
    return render(request,"shop/index.html",context)
