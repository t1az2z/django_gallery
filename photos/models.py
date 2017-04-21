from django.db import models


# Create your models here.
class Photo(models.Model):
    # Класс для отображения фото

    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(
        null=False, blank=False,
        width_field='width', height_field='height', )
    timestamp = models.DateTimeField(auto_now_add=True)
    commentary = models.TextField(max_length=300)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
