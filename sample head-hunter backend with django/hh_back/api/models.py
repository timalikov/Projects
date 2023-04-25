from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="descript")
    city = models.CharField(max_length=255)
    address = models.TextField(default="descript")
    
    def __str__(self) -> str:
        return f"{self.id} : {self.name}"
    
    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "address": self.address,
            # "category": self.category
        }
    

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="description")
    salary = models.FloatField(default=10000)
    company = models.ForeignKey(Company,  on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.id} : {self.name}"

    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "description": self.description,
            "salary": self.salary,
            "company": self.company.to_json()
        }
