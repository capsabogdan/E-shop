from django.contrib.auth import get_user_model

from django.db import models

AuthUserModel = get_user_model()


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(BaseModel):
    class Meta:
        db_table = 'customers'

    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField
    email_address = models.CharField(max_length=255)
    # is_stuff = models.BooleanField(default=False)


class Address(BaseModel):
    class Meta:
        db_table = 'addresses'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField(default=1)
    is_home_address = models.BooleanField()


class Order(BaseModel):
    class Meta:
        db_table = 'orders'

    customer = models.ForeignKey(Customer)
    home_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Product(BaseModel):
    class Meta:
        db_table = 'products'

    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    stock_quantity = models.IntegerField(default=0)
    vat = models.FloatField(default=0.19)


class Products_Ordered(BaseModel):
    class Meta:
        db_table = 'products_ordered'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField(default=0)

