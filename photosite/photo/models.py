from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField

class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    # 이 메소드가 정의된 객체를 지칭하는 URL을 반환/ 메소드 내에서는 reverse() 함수를 호출
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):
    # Album에 연결된 외래 키/ 본 사진이 소속된 앨범 객체를 가리키는 reference 역할
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    # TextField를 사용해 여러 줄의 입력이 가능
    description = models.TextField('Photo Description', blank=True)
    # 필드타입 ThumbnailImageField 사지에 대한 원본 이미지 및 썸네일 이미지를 둘 다 저장/ upload_to 옵션으로 저장할 위치를 지정
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    # 날짜와 시간을 입력하는 필드/ auto_now_add 사지이 처음 업로드 되는 시간을 자동으로 기록
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)

    # 객체 리스트를 출력할 때의 정렬 기준을 정의/ title 컬럼을 기준으로 오름차순으로 정렬
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    # 이 메소드가 정의된 객체를 지칭하는 URL을 반환/ 메소드 내에서는 내장 함수인 reverse()를 호출
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))