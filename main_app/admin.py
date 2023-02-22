from django.contrib import admin
from .models import Novel, Director, Game, Tvshow, Stars

# Register your models here.

admin.site.register(Director)
admin.site.register(Novel)
admin.site.register(Game)
admin.site.register(Tvshow)
admin.site.register(Stars)

