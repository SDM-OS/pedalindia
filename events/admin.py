from django.contrib import admin
import events.models as models

admin.site.register(models.Event)