from django.contrib.auth.models import AbstractUser
from django.db import models


class SizeImage(models.Model):
    """Size for image"""
    name = models.SmallIntegerField(verbose_name='image size')

    def __str__(self):
        return f'{self.name}'


class RateUser(models.Model):
    """Rate for user"""
    name = models.CharField(max_length=64, verbose_name='rate name')
    link = models.BooleanField(verbose_name='link availability')
    size = models.ManyToManyField(SizeImage, verbose_name='size')
    expiration = models.BooleanField(default=False,
                                     verbose_name='link expiration')

    def __str__(self):
        return f'{self.name}'


class HexUser(AbstractUser):
    """Model user"""
    rate = models.ForeignKey(RateUser, models.PROTECT, null=True,
                             verbose_name='rate', related_name='rate')
    email = models.EmailField(max_length=64, blank=True, verbose_name='email')

    def __str__(self):
        return f'{self.username}'
