from rest_framework import serializers

from ..models import Game, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['critic_score', 'critic_count', 'user_score', 'user_count']


class GameSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=False)

    def create(self, validated_data):
        game_instance = Game.objects.create(**validated_data)
        return game_instance

    class Meta:
        model = Game
        fields = [
            'uuid', 'name', 'platform', 'publisher', 'developer',
            'genre', 'year_of_release', 'esrb_rating', 'rating'
        ]
