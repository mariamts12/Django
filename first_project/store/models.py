from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey("self",
                               related_name="+", null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls) -> list:
        categories = Category.objects.all()
        result = []

        for c in categories:
            p = c.parent
            parent = None
            if p is not None:
                parent = {
                    "id": p.id,
                    "name": p.name,
                    "description": p.description
                }

            category = {
                "id": c.id,
                "name": c.name,
                "description": c.description,
                "parent": parent
            }
            result.append(category)
        return result


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls) -> list:
        products = Product.objects.all()
        result = []

        for p in products:
            category_list = []
            for c in p.category.all():
                category = {
                    "id": c.id,
                    "name": c.name,
                    "description": c.description
                }
                category_list.append(category)

            image = str(p.image)
            if len(image) == 0:
                image = None
            product = {
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "price": p.price,
                "image": image,
                "categories": category_list
            }
            result.append(product)
        return result
