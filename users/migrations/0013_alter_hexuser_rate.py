# Generated by Django 3.2.9 on 2021-11-21 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_hexuser_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hexuser',
            name='rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rate', to='users.rateuser', verbose_name='rate'),
        ),
    ]