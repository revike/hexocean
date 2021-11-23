from django.db import models

from users.models import HexUser


class Image(models.Model):
    """Model for images"""
    link = models.ImageField(upload_to='images', verbose_name='link to image')
    user = models.ForeignKey(to=HexUser, on_delete=models.CASCADE,
                             verbose_name='user', related_name='user')
    created_at = models.DateTimeField(auto_now=True, verbose_name='create')

    def __str__(self):
        return f'Image - {self.user} ({self.created_at})'
