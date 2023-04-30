from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Наименование покемона', max_length=200)
    title_en = models.CharField(verbose_name='Наименование покемона на английском', max_length=200, blank=True)
    title_jp = models.CharField(verbose_name='Наименование покемона на японском', max_length=200, blank=True)
    photo = models.ImageField(verbose_name='Фотография покемона', upload_to='pokemon', default='')
    description = models.TextField(verbose_name='Описание покемона', blank=True)
    evolved_from = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="next_evolution", verbose_name='Эволюционировал из')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=None, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(default=None, verbose_name='Время исчезновения')
    level = models.IntegerField(default=0, verbose_name='Уровень')
    health = models.IntegerField(default=0, verbose_name='Здоровье')
    strength = models.IntegerField(default=0, verbose_name='Сила')
    defence = models.IntegerField(default=0, verbose_name='Защита')
    stamina = models.IntegerField(default=0, verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon} @ ({self.lat}, {self.lon})"
