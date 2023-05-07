from rest_framework import serializers

from restapi.models import UsersRank


class RankSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, help_text="User's username"
    )

    class Meta:
        model = UsersRank
        fields = "__all__"
