from django.contrib import admin
from .models import Task, Organization, Catalog, News

admin.site.register(Task)
admin.site.register(Organization)
admin.site.register(Catalog)
admin.site.register(News)
# Register your models here.
