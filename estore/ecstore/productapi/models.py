from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import date,timedelta

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    price = models.PositiveIntegerField()



    def __str__(self):
        return self.name


    def avg_rating(self):
        all_reviews=self.reviews_set.all()
        if all_reviews:
            total=sum([review.rating for review in all_reviews])
            return total/len(all_reviews)
        else:
            return 0
    def review_count(self):
            return  self.reviews_set.all().count()

class Reviews(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])


class Carts(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    qty=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    date=models.DateField(auto_now_add=True)
    options=[
        ("in_cart","in_cart"),
        ("order_placed","order_placed"),
        ("order_cancelled","order_cancelled")
    ]
    status=models.CharField(max_length=20,choices=options,default="in_cart")


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    # date=models.DateField(auto_now_add=True,null=True)
    options=(
        ("order_placed", "order_placed"),
        ("ready_to_ship","ready_to_ship"),
        ("intransit","intransit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=20,choices=options,default="order_placed")
    # edd=date.today()+timedelta(days=5)
    # expected_delivery=models.DateField(null=True,default=edd)
