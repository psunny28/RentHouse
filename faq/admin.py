from django.contrib import admin
from .models import GeneralQuestion, PaymentQuestion, UpgradeQuestion
# Register your models here.

class GeneralQuestionAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'quest', 'answer',)
    list_display_links    =   ('id', 'quest',)

class PaymentQuestionAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'quest', 'answer',)
    list_display_links    =   ('id', 'quest',)

class UpgradeQuestionAdmin(admin.ModelAdmin):
    list_display    =   ('id', 'quest', 'answer',)
    list_display_links    =   ('id', 'quest',)


admin.site.register(GeneralQuestion, GeneralQuestionAdmin)
admin.site.register(PaymentQuestion, PaymentQuestionAdmin)
admin.site.register(UpgradeQuestion, UpgradeQuestionAdmin)
