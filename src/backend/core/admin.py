from django.contrib import admin

from core.models import City, Skill, Organization

admin.site.register(Organization)
admin.site.register(City)
admin.site.register(Skill)

# admin.site.register(EmployerVacancies)
# admin.site.register(EmployerOrganization)
