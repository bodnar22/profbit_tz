from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(unique=True, verbose_name="Имя")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    status = models.CharField(choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock')]
                              , verbose_name="Статус")
    remains = models.IntegerField(verbose_name="Остаток")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Продукты"
