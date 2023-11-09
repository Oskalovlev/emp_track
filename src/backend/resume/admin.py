from django.contrib import admin

from resume.models import (
    Resume,
    SkillInResume,
    Experience,
    Education,
    HigherEducation,
    CourseEducation,
)

# admin.site.register(City)
# admin.site.register(ResumeSkill)


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class SkillInResumeInline(admin.StackedInline):
    model = SkillInResume
    extra = 0


class HigherEducationInline(admin.StackedInline):
    model = HigherEducation
    extra = 0


class CourseEducationInline(admin.StackedInline):
    model = CourseEducation
    extra = 0


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


@admin.register(HigherEducation)
class HigherEducationAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseEducation)
class CourseEducationAdmin(admin.ModelAdmin):
    pass


# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     inlines = (
#         HigherEducationInline,
#         CourseEducationInline
#     )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    # list_display = ("title",)
    inlines = (
        SkillInResumeInline,
        ExperienceInline,
        EducationInline,
    )
