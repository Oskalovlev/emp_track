from rest_framework import serializers

from user.models import User


class EmployerSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя как <Наниматель>."""

    class Meta:
        model = User
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя как <Кандидат>."""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "last_login",
            "is_active",
        )


class CandidateInTrackerSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя как <Кандидат> для трекекра."""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            # "last_login",
        )
