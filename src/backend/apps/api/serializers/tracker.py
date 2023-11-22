from rest_framework import serializers

from tracker.models import Tracker, Comparison, Favorite, Invitation
from api.serializers.resume import ResumeInTrackerSerializer


class TrackerSerializer(serializers.ModelSerializer):
    """Сериализатор модели всех резюме кандидатов."""

    resume = ResumeInTrackerSerializer()

    class Meta:
        model = Tracker
        fields = ("resume",)


class ComparisonSerializer(serializers.ModelSerializer):
    """Сериализатор модели подходящих кандидатов."""

    resume = ResumeInTrackerSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Comparison
        fields = (
            "resume",
            "vacancy",
        )


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор модели избранных кандидатов."""

    resume = ResumeInTrackerSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Favorite
        fields = (
            "resume",
            "vacancy",
        )


class InvitationSerializer(serializers.ModelSerializer):
    """Сериализатор модели приглашенных кандидатов."""

    resume = ResumeInTrackerSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Invitation
        fields = (
            "resume",
            "vacancy",
        )
