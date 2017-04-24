from django.db import models
from .validators import validate_file_extension


class Photo(models.Model):
    # Класс для отображения фото

    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
        null=False, blank=False,
        width_field='width', height_field='height',
        validators=[validate_file_extension])
    timestamp = models.DateTimeField(auto_now_add=True)
    commentary = models.TextField(max_length=300)
    views = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
