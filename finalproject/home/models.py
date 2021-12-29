from django.db import models


# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    cost = models.IntegerField()

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.name


class recharge(models.Model):
    cost = models.ForeignKey(customer, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=100)
    number_card = models.IntegerField()
    seri = models.IntegerField()

    class Meta:
        db_table = "recharge"

    def __str__(self):
        return self.name


class category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class product(models.Model):
    type = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    img = models.ImageField()
    cost = models.CharField(max_length=100)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class detail(models.Model):
    type = models.ForeignKey(product, on_delete=models.CASCADE)
    img = models.ImageField()
    name = models.CharField(max_length=100)
    img = models.ImageField()
    cost = models.CharField(max_length=100)

    class Meta:
        db_table = "detail"

    def __str__(self):
        return self.name


class news(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=100)
    img = models.ImageField()
    text = models.TextField()

    class Meta:
        db_table = "news"

    def __str__(self):
        return self.name
