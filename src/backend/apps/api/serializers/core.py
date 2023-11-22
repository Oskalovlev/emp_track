from rest_framework import serializers

from core.models import City, Skill, Organization


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор модели города."""

    name = serializers.PrimaryKeyRelatedField(
        source="city",
        read_only=True,
    )

    class Meta:
        model = City
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор модели навыка."""

    name = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all())

    class Meta:
        model = Skill
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор модели организации."""

    name = serializers.PrimaryKeyRelatedField(
        source="organization",
        read_only=True,
    )

    class Meta:
        model = Organization
        fields = "__all__"
