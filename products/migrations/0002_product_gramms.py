# Generated by Django 4.1.2 on 2023-05-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gramms',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
