# Generated by Django 3.2.9 on 2021-11-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211119_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='rate name')),
                ('link', models.BooleanField(verbose_name='link availability')),
                ('size', models.IntegerField(verbose_name='image size')),
                ('expiration', models.IntegerField(default=0, verbose_name='link expiration (min)')),
            ],
        ),
        migrations.RemoveField(
            model_name='hexuser',
            name='is_base',
        ),
        migrations.RemoveField(
            model_name='hexuser',
            name='is_enterprise',
        ),
        migrations.RemoveField(
            model_name='hexuser',
            name='is_premium',
        ),
    ]