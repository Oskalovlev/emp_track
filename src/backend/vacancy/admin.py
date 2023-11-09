from django.contrib import admin

from vacancy.models import (
    Vacancy,
    SkillInVacancy,
    EmployerProfile,
    VacancyInProfile,
)


class SkillInVacancyInline(admin.StackedInline):
    model = SkillInVacancy
    extra = 0


class VacancyInProfileInline(admin.StackedInline):
    model = VacancyInProfile
    extra = 0


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "position",
        "specialty",
        "description",
        "city",
    )
    search_fields = (
        "position",
        "specialty",
        "city",
    )
    list_filter = (
        "specialty",
        "city",
    )
    empty_value_display = "--пусто--"
    inlines = (SkillInVacancyInline,)


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "employer",
        "organization",
    )
    search_fields = (
        "employer",
        "organization",
    )
    list_filter = ("employer",)
    empty_value_display = "--пусто--"
    inlines = (VacancyInProfileInline,)


# @admin.register(SkillInVacancy)
# class SkillInVacancyAdmin(admin.ModelAdmin):
#     list_display = (
#         "skill",
#         "vacancy",
#     )
#     search_fields = (
#         "skill",
#         "vacancy",
#     )
#     list_filter = ("skill",)
#     empty_value_display = "--пусто--"


# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ("name",)


# class JobSkillInline(admin.TabularInline):
#     model = JobSkill
#     extra = 0


# @admin.register(JobTitle)
# class JobTitleAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     inlines = (JobSkillInline,)
