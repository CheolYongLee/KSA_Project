from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField, ThumbnailImageFieldFile
import service

class Album(models.Model):
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField('IMAGE', upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)
<<<<<<< HEAD
    result = models.CharField('지문정보', max_length=30, blank=True)
=======
    # result = image
>>>>>>> 296790c2cd1804b7423a9196ed9fa48c63905496

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

<<<<<<< HEAD
    def get_result(self):
        return reverse('photo:photo_detail', args=(self.result, service.ImageService))

=======
>>>>>>> 296790c2cd1804b7423a9196ed9fa48c63905496

