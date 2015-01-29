from django.db import models
from django.utils import timezone


BRACKET_SIZES = (
  (4, 'Four'),
  (8, 'Eight'),
  (16, 'Sixteen')
)

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    players = models.ManyToManyField('Player', blank=True, null=True)

    max_players = models.PositiveIntegerField(choices=BRACKET_SIZES, default=4)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        get_latest_by = "created"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.players.count() == self.max_players:
            if self.match_set.count() == 0:
                players = list(self.players.order_by('?'))

                while players:
                    m = Match.objects.create(player_one=players.pop(),
                                             player_two=players.pop(),
                                             tournament=self)
                    m.save()

        super(Tournament, self).save(*args, **kwargs)


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Match(models.Model):
    tournament = models.ForeignKey('Tournament')
    player_one = models.ForeignKey('Player')
    player_two = models.ForeignKey('Player', related_name='player_two')
    winner = models.ForeignKey('Player', related_name='winner', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'matches'

    def __unicode__(self):
        if self.winner:
            return '{} defeated {}'.format(self.winner, self.player_one if self.player_two == self.winner else self.player_two)
        return '{} vs {}'.format(self.player_one.name, self.player_two.name)
