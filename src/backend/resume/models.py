# from datetime import date

from django.db import models
from django.conf import settings

from backend.user.models import User
from backend.core.models import Skill, City

# from vacancy.models import Vacancy


class Resume(models.Model):
    """Модель резюме."""

    title = models.CharField(
        "Заголовок",
        max_length=settings.MAX_LENGTH,
    )
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Кандидат",
    )
    photo = models.ImageField(
        "Фото",
        upload_to="photo/",
        default=None,
    )
    gender = models.CharField(
        choices=settings.GENDER_FLAG,
        verbose_name="Пол",
    )
    grade = models.CharField(
        "Уровень",
        max_length=settings.MAX_LENGTH,
    )
    birthday = models.DateField(
        "День рождения",
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        verbose_name="Город",
    )
    # grade = models.CharField("Грейд")
    # city = models.CharField("Город", max_length=50)
    telegram = models.CharField(
        "Телеграм",
        max_length=50,
    )
    github = models.CharField(
        "GitHub",
        max_length=50,
    )
    portfolio = models.CharField("Портфолио", max_length=50)
    about_me = models.TextField(
        "О себе",
    )
    type_work = models.PositiveSmallIntegerField(
        "Тип работы",
        choices=settings.TYPE_WORK,
        default=settings.ZERO,
    )
    status_finded = models.PositiveSmallIntegerField(
        "Статус",
        choices=settings.STATUS_FIDED,
        default=settings.ZERO,
    )
    date_created = models.DateTimeField(
        "Создание резюме",
        auto_now=True,
    )

    class Meta:
        ordering = ["candidate"]
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        default_related_name = "resumes"

    def __str__(self):
        return f"{self.candidate}" if hasattr(self, "candidate") else ""

    # def get_age(self) -> int:
    #     """Получить возраст кандидата."""
    #     return (date.today() - self.birthday).year

    # get_age.short_description = "Возраст"

    # def get_main_skills(
    #     self, vacancy: Vacancy, amount: int
    # ) -> list[(Skill, int),]:
    #     """
    #     Определение главных скилов для вакансии.

    #     Приходит:
    #     vacancy - Вакансия
    #     amount - число главных скилов

    #     Уходит:
    #     Список пар:
    #     Skill - id? name?
    #     rating - значение соотв. навыка
    #     """
    #     return [("Навык 1", 100), ("Навык 5", 80), ("Навык 3", 70)]

    # get_age.short_description = "Главные Навыки"


class SkillInResume(models.Model):
    skill = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Скилл",
        related_name="+",
    )
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Резюме",
        related_name="skill_list",
    )

    class Meta:
        ordering = ("resume",)
        verbose_name = "Скилл в резюме"
        verbose_name_plural = "Скиллы в резюме"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "skill",
                    "resume",
                ),
                name="unique_skill_resume",
            ),
        )

    def __str__(self):
        return f"{self.skill} в {self.resume}"


class Experience(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Опыт",
        related_name="experiences",
    )

    position = models.CharField(
        verbose_name="Должность",
        max_length=settings.MAX_LENGTH,
    )
    period = models.DurationField("Период")
    duties = models.TextField(
        verbose_name="Обязанности",
    )

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"

    def __str__(self):
        return f"{self.position}"


class BaseEducationModel(models.Model):
    name = models.CharField(
        "Название",
        max_length=settings.MAX_LENGTH,
    )
    speciality = models.CharField(
        "Специальность",
        max_length=settings.MAX_LENGTH,
    )
    period = models.CharField(
        "Период",
        max_length=settings.MAX_LENGTH,
    )

    class Meta:
        abstract = True


class HigherEducation(BaseEducationModel):

    institution = models.CharField(
        "Учебное заведение",
        max_length=settings.MAX_LENGTH,
    )

    class Meta:
        verbose_name = "Высшее образование"
        verbose_name_plural = "Высшие образования"


class CourseEducation(BaseEducationModel):
    class Meta:
        verbose_name = "Дополнительное образование"
        verbose_name_plural = "Дополнительные образования"


class Education(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="educations",
        verbose_name="Образование",
    )
    higher = models.ForeignKey(
        HigherEducation,
        on_delete=models.CASCADE,
        related_name="educations",
    )
    course = models.ForeignKey(
        CourseEducation,
        on_delete=models.CASCADE,
        related_name="educations",
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

    def __str__(self):
        return f"{self.institution}"
