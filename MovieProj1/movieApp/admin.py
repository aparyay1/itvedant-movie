from django.contrib import admin
from movieApp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['rel_date','movname','actorname','actressname','rating']
admin.site.register(Movie,MovieAdmin)
