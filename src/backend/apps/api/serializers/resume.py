from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, relations

from core.models import Skill
from resume.models import Resume, SkillInResume
from api.serializers.user import (
    CandidateSerializer,
    CandidateInTrackerSerializer,
)
from api.serializers.core import CitySerializer


class SkillInResumeSerializer(serializers.ModelSerializer):
    """Сериализатор модели навыка в резюме."""

    name = serializers.SlugRelatedField(
        source="skill", read_only=True, slug_field="name"
    )

    class Meta:
        model = SkillInResume
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    photo = Base64ImageField()
    skill_list = SkillInResumeSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"


class ResumeInTrackerSerializer(serializers.ModelSerializer):
    candidate = CandidateInTrackerSerializer(read_only=True)
    photo = Base64ImageField(read_only=True)
    grade = serializers.CharField()
    skill_list = SkillInResumeSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ("candidate", "photo", "grade", "skill_list")


class ResumeCreateSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    photo = Base64ImageField(max_length=None, use_url=True)
    city = CitySerializer(read_only=True)
    skill_list = relations.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Resume
        fields = (
            "title",
            "candidate",
            "photo",
            "birthday",
            "city",
            "skill_list",
            "gender",
            "telegram",
            "github",
            "about_me",
            "type_work",
            "status_finded",
        )
        read_only_fields = ("author",)

    @atomic
    def creating_skills(self, resume, skills_data):
        for skill in skills_data:
            SkillInResume.objects.get_or_create(
                resume=resume,
                skill=skill["id"],
            )

    @atomic
    def create(self, validated_data):
        skills_data = validated_data.pop("skills")
        candidate = self.context.get("request").user
        resume = Resume.objects.create(candidate=candidate, **validated_data)
        self.creating_skills(resume, skills_data)

        return resume

    @atomic
    def update(self, instance, validated_data):
        skills_data = validated_data.pop("skills")
        SkillInResume.objects.filter(resume=instance).delete()
        self.creating_skills(instance, skills_data)

        return super().update(instance, validated_data)
