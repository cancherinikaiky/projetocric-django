from django.contrib import admin
from event.models import Enrollment, Bond
from .enrollmentform import EnrollmentForm


class BondAdmin(admin.ModelAdmin):
    ordering = ['name']

class EnrollmentAdmin(admin.ModelAdmin):
    form = EnrollmentForm
    list_display = ('full_name', 'date_of_birth', 'get_bond_choice_display', 'how_knew', 'rg',)

admin.site.register(Bond, BondAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
