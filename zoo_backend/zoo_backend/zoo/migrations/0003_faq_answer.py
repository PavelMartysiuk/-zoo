# Generated by Django 4.1.2 on 2022-10-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_rename_workers_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
    ]
