# Generated by Django 3.1 on 2020-12-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20201219_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.FileField(upload_to='articulos/'),
        ),
    ]
