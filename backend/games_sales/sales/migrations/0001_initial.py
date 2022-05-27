# Generated by Django 4.0.4 on 2022-05-11 14:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('NA_sales', models.FloatField(blank=True, help_text='Game Sales in North America (in millions of units)', null=True)),
                ('EU_sales', models.FloatField(blank=True, help_text='Game Sales in the European Union (in millions of units)', null=True)),
                ('JP_sales', models.FloatField(blank=True, help_text='Game Sales in Japan (in millions of units)', null=True)),
                ('other_sales', models.FloatField(blank=True, help_text='Game Sales in the rest of the world, i.e. Africa, Asiaexcluding Japan, Australia, Europe excluding the E.U. and', null=True)),
                ('global_sales', models.FloatField(blank=True, help_text='Total Sales in the world (in millions of units)', null=True)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
