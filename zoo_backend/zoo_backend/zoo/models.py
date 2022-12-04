import os

from django.db import models

from core.models.utils import ModelMethods
from core.validators.model_validators import SizeValidators
from core.enum.animal import GenderEnum


class Country(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(null=True,
                              upload_to=ModelMethods.get_upload_path,
                              blank=True,
                              validators=[SizeValidators.image_size_validator], )

    def image_path(self):
        return os.path.join(f'country_photo/{self.id}')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(null=True,
                              upload_to=ModelMethods.get_upload_path,
                              blank=True,
                              validators=[SizeValidators.image_size_validator], )
    description = models.TextField()
    country = models.ForeignKey(
        'Country',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='animals'
    )

    def image_path(self):
        return os.path.join(f'category_photo/{self.id}')

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(null=True,
                              upload_to=ModelMethods.get_upload_path,
                              blank=True,
                              validators=[SizeValidators.image_size_validator], )
    gender = models.CharField(choices=GenderEnum.items(), max_length=10)
    date_of_birth = models.DateField()
    weight = models.FloatField()
    favorite_food = models.TextField()

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='animals'
    )

    def image_path(self):
        return os.path.join(f'animal_photo/{self.id}')

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(
        null=True,
        upload_to=ModelMethods.get_upload_path,
        blank=True,
        validators=[SizeValidators.image_size_validator],
    )

    def image_path(self):
        return os.path.join(f'worker_photo/{self.id}')

    def __str__(self):
        return f"{self.name} {self.last_name}"


class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
