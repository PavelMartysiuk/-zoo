# Generated by Django 4.1.2 on 2022-11-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0006_alter_category_name_alter_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]