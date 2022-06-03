from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class GeneralQuestion(models.Model):
    quest   =   models.TextField()
    answer   =   RichTextField()

    # class Meta:
    #     verbose_name    =   'faq'
    #     verbose_name_plural =   'FAQ'

    def __str__(self):
        return self.quest

class PaymentQuestion(models.Model):
    quest   =   models.TextField()
    answer   =   RichTextField()

    # class Meta:
    #     verbose_name    =   'faq'
    #     verbose_name_plural =   'FAQ'

    def __str__(self):
        return self.quest

class UpgradeQuestion(models.Model):
    quest   =   models.TextField()
    answer   =   RichTextField()

    # class Meta:
    #     verbose_name    =   'faq'
    #     verbose_name_plural =   'FAQ'

    def __str__(self):
        return self.quest
