# Generated by Django 3.2.9 on 2021-11-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20211121_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeimage',
            name='name',
            field=models.SmallIntegerField(verbose_name='image size'),
        ),
    ]