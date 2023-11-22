from django.db import models
from django.conf import settings

from user.models import User
from core.models import City, Skill, Organization
from services.choices import CURRENCY


class Vacancy(models.Model):
    """Модель Вакансии."""

    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Наниматель",
    )
    wages_from = models.PositiveIntegerField()
    wages_to = models.PositiveIntegerField()
    currency = models.CharField(
        choices=CURRENCY,
    )
    position = models.CharField(
        "Должность",
        max_length=settings.MAX_LENGTH,
    )
    specialty = models.CharField(
        "Специализация",
        max_length=settings.MAX_LENGTH,
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    duties = models.CharField(
        "Обязанности",
        max_length=settings.MAX_LENGTH,
    )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, verbose_name="Город"
    )
    conditions = models.CharField(
        "Условия",
        max_length=settings.MAX_LENGTH,
    )
    stages = models.CharField(
        "Этапы отбора",
        max_length=settings.MAX_LENGTH,
    )

    class Meta:
        ordering = ("position",)
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        default_related_name = "vacancys"

    def __str__(self):
        return self.position


class SkillInVacancy(models.Model):
    """Модель скилла в вакансии."""

    skill = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        verbose_name="Скилл",
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name="skill_list",
        verbose_name="Вакансия",
    )

    class Meta:
        ordering = ("vacancy",)
        verbose_name = "Скилл в вакансии"
        verbose_name_plural = "Скилы в вакансии"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "skill",
                    "vacancy",
                ),
                name="unique_skill_vacancy",
            ),
        )

    def __str__(self):
        return f"{self.skill} в {self.vacancy}"


class EmployerProfile(models.Model):
    employer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Наниматель"
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="организация",
    )

    class Meta:
        ordering = ("employer",)
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        default_related_name = "profiles"

    def __str__(self):
        return self.employer


class VacancyInProfile(models.Model):
    profile = models.ForeignKey(
        EmployerProfile,
        on_delete=models.CASCADE,
        related_name="vacancy_list",
        verbose_name="Профиль",
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        verbose_name="Вакансия",
    )

    class Meta:
        ordering = ("profile",)
        verbose_name = "Вакансия в профиле"
        verbose_name_plural = "Вакансии в профиле"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "vacancy",
                    "profile",
                ),
                name="unique_vacancy_profile",
            ),
        )

    def __str__(self):
        return f"{self.vacancy} в {self.profile}"
