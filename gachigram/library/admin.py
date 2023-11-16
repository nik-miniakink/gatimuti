from django.contrib import admin

from library.models import Actor, Gender, Movie, MovieGenres, Nationalities

admin.site.register(Actor)
admin.site.register(Gender)
admin.site.register(Movie)
admin.site.register(MovieGenres)
admin.site.register(Nationalities)
