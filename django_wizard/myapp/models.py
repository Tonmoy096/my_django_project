from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default = 'No description provided')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username



'''
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.IntegerField()
    category = models.ForeignKey('category', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username'''


'''class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name'''