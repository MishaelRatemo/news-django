from django.contrib import admin
from .models import Editor,Article,tags

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):#inherits from the ModelAdmin class
    filter_horizontal =('tags',) #allows ordering of many to many fields and pass in the tags article field

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)