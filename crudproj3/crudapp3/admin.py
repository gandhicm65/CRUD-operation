from django.contrib import admin
from crudapp3.models import Person
# Register your models here.
class PersonAdm(admin.ModelAdmin):
    Per = ['Name','Age','Contact','Location']
admin.site.register(Person, PersonAdm)