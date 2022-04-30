from django.contrib import admin
from .models import EXAM,QUESTION,OPTION,ANSWER

# Register your models here.

class EXAMAdmin(admin.ModelAdmin):
    pass
admin.site.register(EXAM, EXAMAdmin)

class QUESTIONAdmin(admin.ModelAdmin):
    pass
admin.site.register(QUESTION, QUESTIONAdmin)


class OPTIONAdmin(admin.ModelAdmin):
    pass
admin.site.register(OPTION, OPTIONAdmin)


class ANSWERAdmin(admin.ModelAdmin):
    pass
admin.site.register(ANSWER, ANSWERAdmin)