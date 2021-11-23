from django.contrib import admin

from main.models import Image
from users.models import SizeImage

admin.site.register(Image)
admin.site.register(SizeImage)
