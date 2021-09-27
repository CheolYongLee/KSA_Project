from django.contrib import admin
from photo.models import Album, Photo

# 앨범 객체를 보여줄 때 객체에 연결된 사진 객체들을 같이 보여줄 수 있음/ StackedInline 세로로 나열, TabularInline 테이블 모양처럼 행으로 나열
class PhotoInline(admin.StackedInline):
    # 추가로 보여주는 테이블은 Photo 테이블
    model = Photo
    # 이미 존재하는 객체 외에 추가로 입력할 수 있는 Photo 테이블의 객체의 수는 2개
    extra = 2

@admin.register(Album)
class AlbumAdmin(Album):
    # 앨범 객체 수정 화면을 보여줄 때 PhotoInline 클래스에 정의한 사항을 같이 보여줌
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')

# Photo와 PhotoAdmin 클래스를 등록할 때 admin.site.register() 함수를 사용해도 되지만 데코레이터를 사용하면 좀 더 간단함
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')