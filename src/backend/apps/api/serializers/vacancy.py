from django.db.transaction import atomic
from rest_framework import serializers, relations

from core.models import Skill
from vacancy.models import Vacancy, SkillInVacancy
from api.serializers.user import EmployerSerializer
from api.serializers.core import CitySerializer


class SkillInVacancySerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(read_only=True, source="skill")

    class Meta:
        model = SkillInVacancy
        fields = "__all__"


# class VacancySerializer(serializers.ModelSerializer):
#     position = serializers.SlugRelatedField(
#         source="vacancy", read_only=True, slug_field="position"
#     )

#     class Meta:
#         model = Vacancy
#         fields = ("position",)


class VacancyReadListSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(
        source="vacancy", read_only=True, slug_field="position"
    )

    class Meta:
        model = Vacancy
        fields = ("position",)


class VacancyCreateSerializer(serializers.ModelSerializer):
    author = EmployerSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    skill_list = relations.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Vacancy
        fields = (
            "position",
            "author",
            "specialty",
            "description",
            "duties",
            "city",
            "conditions",
            "stages",
            "skill_list",
        )
        read_only_fields = ("author",)

    @atomic
    def creating_skills(self, vacancy, skills_data):
        for skill in skills_data:
            SkillInVacancy.objects.get_or_create(
                vacancy=vacancy,
                skill=skill["id"],
            )

    @atomic
    def create(self, validated_data):
        skills_data = validated_data.pop("skills")
        author = self.context.get("request").user
        vacancy = Vacancy.objects.create(author=author, **validated_data)
        self.creating_skills(vacancy, skills_data)

        return vacancy

    @atomic
    def update(self, instance, validated_data):
        skills_data = validated_data.pop("skills")
        SkillInVacancy.objects.filter(vacancy=instance).delete()
        self.creating_skills(instance, skills_data)

        return super().update(instance, validated_data)
