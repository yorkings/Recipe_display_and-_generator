from django.contrib import admin
from .models import *
# Register your models here.
class ProfileModel(admin.ModelAdmin):
    list_display= ['user','bios','image']
    list_filter=['user','bios','image']
    search_fields=['name']
admin.site.register(Profile,ProfileModel)    

class PostAdmin(admin.ModelAdmin):
    # list_display=['']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment,CommentAdmin)

class CosmeticsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cosmetics,CosmeticsAdmin)

class LearningAdmin(admin.ModelAdmin):
    pass
admin.site.register(Learning,LearningAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category,CategoryAdmin)
