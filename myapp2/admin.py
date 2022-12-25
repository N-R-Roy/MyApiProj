from django.contrib import admin

from . import models


admin.site.register(models.PersonInfo)
admin.site.register(models.Singer)
admin.site.register(models.Song)
admin.site.register(models.Group)

