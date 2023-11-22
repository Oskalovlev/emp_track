from datetime import date

from django.db import models

from user.models import User
from core.models import Skill, City
from services.constants.models import MAX_LENGTH, ZERO
from services.choices import GENDER_FLAG, TYPE_WORK, STATUS_FIDED

# from vacancy.models import Vacancy


class Resume(models.Model):
    """Модель резюме."""

    title = models.CharField(
        "Заголовок",
        max_length=MAX_LENGTH,
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
        null=True,
    )
    gender = models.CharField(
        "Пол",
        choices=GENDER_FLAG,
    )
    grade = models.CharField(
        "Уровень",
        max_length=MAX_LENGTH,
        null=True,
    )
    birthday = models.DateField(
        "День рождения",
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Город",
    )
    # grade = models.CharField("Грейд")
    # city = models.CharField("Город", max_length=50)
    telegram = models.CharField(
        "Телеграм",
        max_length=MAX_LENGTH,
        null=True,
    )
    github = models.CharField(
        "GitHub",
        max_length=MAX_LENGTH,
        null=True,
    )
    portfolio = models.CharField(
        "Портфолио",
        max_length=MAX_LENGTH,
        null=True,
    )
    about_me = models.TextField(
        "О себе",
    )
    type_work = models.PositiveSmallIntegerField(
        "Тип работы",
        choices=TYPE_WORK,
        default=ZERO,
    )
    status_finded = models.PositiveSmallIntegerField(
        "Статус",
        choices=STATUS_FIDED,
        default=ZERO,
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

    def get_age(self) -> int:
        """Получить возраст кандидата."""
        return (date.today() - self.birthday).year


class SkillInResume(models.Model):
    """Модель скилла в резюме."""

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
    """Модель опыта кандидата."""

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Опыт",
        related_name="experiences",
    )

    position = models.CharField(
        verbose_name="Должность",
        max_length=MAX_LENGTH,
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
    """Абстрактная модель базовых полей <образования>."""

    name = models.CharField(
        "Название",
        max_length=MAX_LENGTH,
    )
    speciality = models.CharField(
        "Специальность",
        max_length=MAX_LENGTH,
    )
    period = models.CharField(
        "Период",
        max_length=MAX_LENGTH,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HigherEducation(BaseEducationModel):
    """Модель высшего образования."""

    class Meta:
        verbose_name = "Высшее образование"
        verbose_name_plural = "Высшие образования"


class CourseEducation(BaseEducationModel):
    """Модель дополнительного образования/курсов."""

    class Meta:
        verbose_name = "Дополнительное образование"
        verbose_name_plural = "Дополнительные образования"


class Education(models.Model):
    """Модель образования."""

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
        verbose_name="Высшее бразование",
    )
    course = models.ForeignKey(
        CourseEducation,
        on_delete=models.CASCADE,
        related_name="educations",
        verbose_name="Доп. образование",
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"
