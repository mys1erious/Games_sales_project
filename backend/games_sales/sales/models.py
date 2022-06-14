import uuid as uuid_lib
from django.db import models
from games.models import Game
from core.models import TimeStampedModel


class SaleManager(models.Manager):
    def create(self, **obj_data):
        game_data = obj_data.pop('game')
        game_instance = Game.objects.create(**game_data)
        obj_data['game'] = game_instance

        return super().create(**obj_data)


class Sale(TimeStampedModel):
    uuid = models.UUIDField(
        db_index=True,
        unique=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    game = models.OneToOneField(
        Game, on_delete=models.CASCADE
    )
    NA_sales = models.FloatField(
        help_text='Game Sales in North America (in millions of units)',
        null=True, blank=True
    )
    EU_sales = models.FloatField(
        help_text='Game Sales in the European Union (in millions of units)',
        null=True, blank=True
    )
    JP_sales = models.FloatField(
        help_text='Game Sales in Japan (in millions of units)',
        null=True, blank=True
    )
    other_sales = models.FloatField(
        help_text='Game Sales in the rest of the world, i.e. Africa, Asia'
                  'excluding Japan, Australia, Europe excluding the E.U. and',
        null=True, blank=True
    )
    global_sales = models.FloatField(
        help_text='Total Sales in the world (in millions of units)',
        null=True, blank=True
    )

    objects = SaleManager()

    def __str__(self):
        return f'{self.game}'
