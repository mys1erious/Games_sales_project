import uuid as uuid_lib

from django.db import models


class Rating(models.Model):
    critic_score = models.FloatField(
        help_text='Aggregate score compiled by Metacritic staff',
        null=True, blank=True)
    critic_count = models.FloatField(
        help_text='The number of critics used in coming up with the Critic_score',
        null=True, blank=True)
    user_score = models.FloatField(
        help_text='Score by Metacritic`s subscribers',
        null=True, blank=True)
    user_count = models.FloatField(
        help_text='Number of users who gave the user_score',
        null=True, blank=True)


class GameManager(models.Manager):
    def create(self, **obj_data):
        rating_data = obj_data.pop('rating')
        rating_instance = Rating.objects.create(**rating_data)
        obj_data['rating'] = rating_instance

        return super().create(**obj_data)


class Game(models.Model):
    class ESRBRatings(models.TextChoices):
        KA = 'K-A', 'Kids to Adults, 6+'
        M = 'M', 'Mature, 17+'
        RP = 'RP', 'Rating Pending'
        E = 'E', 'Everyone'
        AO = 'AO', 'Adults Only, 18+'
        E10PLUS = 'E10+', 'Everyone 10+'
        EC = 'EC', 'Early Childhood, 3+'
        T = 'T', 'Teen, 13+'

    uuid = models.UUIDField(
        db_index=True,
        unique=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=120
    )
    platform = models.CharField(
        max_length=30,
        null=True, blank=True
    )
    publisher = models.CharField(
        max_length=120,
        null=True, blank=True
    )
    developer = models.CharField(
        max_length=120,
        null=True, blank=True
    )
    genre = models.CharField(
        max_length=30,
        null=True, blank=True
    )
    year_of_release = models.IntegerField(
        null=True, blank=True
    )
    rating = models.OneToOneField(
        Rating,
        on_delete=models.PROTECT,
        null=True
    )

    #  Later restrict to only Choices
    esrb_rating = models.CharField(
        max_length=4,
        null=True, blank=True,
        choices=ESRBRatings.choices
    )

    objects = GameManager()

    def __str__(self):
        return f'{self.name}'
