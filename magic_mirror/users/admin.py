from django.contrib import admin
from film.models import *
from users.models import *
# Register your models here.
admin.site.register(Movie)
admin.site.register(Tag)
admin.site.register(Preview)
admin.site.register(MovieCol)


admin.site.register(UserLog)
admin.site.register(UserProfile)


