from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=100, default='green')

    @property
    def limit(self):
        return self.budget.limit

    def purchases_in_month(self, month, year):
        return self.purchase_set.filter(date__year=year, date__month=month)

    def total_in_month(self, month, year):
        return sum([purchase.price for purchase in self.purchases_in_month(month, year)])

    def __str__(self):
        return self.name


class Purchase(models.Model):
    date = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=CASCADE)

    def __str__(self):
        return f'{self.category} {self.price}€'


class Budget(models.Model):
    limit = models.FloatField()
    category = models.OneToOneField('Category', on_delete=CASCADE)

    def __str__(self):
        return f'Budget pour {self.category.name}'

