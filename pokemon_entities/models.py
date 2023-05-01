from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Наименование покемона', max_length=200)
    title_en = models.CharField(verbose_name='Наименование покемона на английском', max_length=200, blank=True)
    title_jp = models.CharField(verbose_name='Наименование покемона на японском', max_length=200, blank=True)
    photo = models.ImageField(verbose_name='Фотография покемона', upload_to='pokemon')
    description = models.TextField(verbose_name='Описание покемона', blank=True)
    evolved_from = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='next_evolutions', verbose_name='Эволюционировал из')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, verbose_name='Покемон',
                                related_name='entities')
    lat = models.FloatField(null=True, verbose_name='Широта', blank=True)
    lon = models.FloatField(null=True, verbose_name='Долгота', blank=True)
    appeared_at = models.DateTimeField(null=True, verbose_name='Время появления', blank=True)
    disappeared_at = models.DateTimeField(null=True, verbose_name='Время исчезновения', blank=True)
    level = models.IntegerField(null=True, verbose_name='Уровень', blank=True)
    health = models.IntegerField(null=True, verbose_name='Здоровье', blank=True)
    strength = models.IntegerField(null=True, verbose_name='Сила', blank=True)
    defence = models.IntegerField(null=True, verbose_name='Защита', blank=True)
    stamina = models.IntegerField(null=True, verbose_name='Выносливость', blank=True)

    def __str__(self):
        return f'{self.pokemon} @ ({self.lat}, {self.lon})'
