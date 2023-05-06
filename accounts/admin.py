from django.contrib import admin
from .models import profile,authors,books
# Register your models here.
admin.site.register(profile)
admin.site.register(authors)
admin.site.register(books)