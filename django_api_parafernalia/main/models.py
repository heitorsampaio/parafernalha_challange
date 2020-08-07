from django.db import models
from .validators import validate_idade_minima

# Create your models here.


class Products(models.Model):

    price = models.FloatField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    base_discount_percent = models.FloatField()

    class Meta:
        db_table = 'products'

        constraints = [
            models.CheckConstraint(check=models.Q(
                base_discount_percent__lte=25.0), name='base_discount_max')
        ]

    def __str__(self):
        return self.title


class Users(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(verbose_name="Birthdate", validators=[validate_idade_minima])

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.frist_name
