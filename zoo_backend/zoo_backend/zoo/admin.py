from django.contrib import admin

# Register your models here.

from zoo.models import Category, Animal, About, FAQ, Country, Worker

admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(About)
admin.site.register(FAQ)
admin.site.register(Country)
admin.site.register(Worker)