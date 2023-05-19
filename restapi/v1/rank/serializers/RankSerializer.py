from rest_framework import serializers

from restapi.models import UsersRank
from restapi.v1.users.serializers.UserSerializer import UserFullSerializer


class RankSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        required=True, help_text="User's username"
    )

    class Meta:
        model = UsersRank
        fields = "__all__"


class UserRankFullSerializer(serializers.ModelSerializer):
    user = UserFullSerializer()

    class Meta:
        model = UsersRank
        fields = "__all__"
