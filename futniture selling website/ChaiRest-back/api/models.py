from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
        }


class Furniture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='furniture')
    price = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'category': self.category.id,
            'price': self.price,
        }


class Order(models.Model):
    address = models.TextField(max_length=255)
    phoneNumber = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE, related_name='order')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def to_json(self):
        return {
            'id': self.id,
            'address': self.address,
            'phoneNumber': self.phoneNumber,
            'user': self.user.id,
            'furniture': self.furniture.id,
        }
