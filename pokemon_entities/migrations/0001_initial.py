# Generated by Django 3.1.14 on 2023-04-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='', upload_to='pokemon')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('appeared_at', models.DateTimeField(default=None)),
                ('disappeared_at', models.DateTimeField(default=None)),
                ('level', models.IntegerField(default=0)),
                ('health', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=0)),
                ('defence', models.IntegerField(default=0)),
                ('stamina', models.IntegerField(default=0)),
                ('pokemon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
