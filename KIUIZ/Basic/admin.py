from django.contrib import admin
from .models import EXAM,QUESTION,OPTION,ANSWER,RESPONSE

# Register your models here.

class EXAMAdmin(admin.ModelAdmin):
    pass
admin.site.register(EXAM, EXAMAdmin)

class QUESTIONAdmin(admin.ModelAdmin):
    list_display = ('query','exam')

admin.site.register(QUESTION, QUESTIONAdmin)


class OPTIONAdmin(admin.ModelAdmin):
    list_display = ('question','option')
admin.site.register(OPTION, OPTIONAdmin)


class ANSWERAdmin(admin.ModelAdmin):
    list_display = ('question','solution')
admin.site.register(ANSWER, ANSWERAdmin)



class RESPONSEAdmin(admin.ModelAdmin):
    list_display = ('exam','studentRollNumber','question','response','date_time')
admin.site.register(RESPONSE,RESPONSEAdmin)
