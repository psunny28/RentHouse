from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeCanvas, ResizeToFill
from django.utils.html import mark_safe
from imagekit.processors import ResizeCanvas, ResizeToFill
from ckeditor.fields import RichTextField

# Create your models here.
class service(models.Model):
    title    =   models.CharField(max_length=800)
    details   =   RichTextField()

    class Meta:
        verbose_name    =   'service'
        verbose_name_plural =   'service'

    def __str__(self):
        return self.title

class homepage(models.Model):
    resent_properties        =  RichTextField(blank=True)
    how_works_property        =  RichTextField(blank=True)
    how_works_agent        =  RichTextField(blank=True)
    how_works_deal        =  RichTextField(blank=True)
    featured_properties        =  RichTextField(blank=True)
    explore_agents        =  RichTextField(blank=True)
    find_by_location        =  RichTextField(blank=True)
    apps    =   RichTextField(blank=True)

    class Meta:
        verbose_name    =   'homepage'
        verbose_name_plural =   'homepage'

    def __str__(self):
        return self.resent_properties

class membership_page(models.Model):
    owner_plans     =  RichTextField(blank=True)
    tenant_plans     =  RichTextField(blank=True)

    class Meta:
        verbose_name    =   'membership_page'
        verbose_name_plural =   'membership_page'

    def __str__(self):
        return self.owner_plans

class aboutus(models.Model):
    our_story   =   RichTextField(blank=True)
    our_mission   =   RichTextField(blank=True)
    security   =   RichTextField(blank=True)
    manage   =   RichTextField(blank=True)
    promise   =   RichTextField(blank=True)

    class Meta:
        verbose_name    =   'aboutus'
        verbose_name_plural =   'About Us'

    def __str__(self):
        return self.our_story

class TeamMember(models.Model):
    name    =   models.CharField(max_length=100)
    designation =   models.CharField(max_length=100)
    facebook_link   =   models.URLField(max_length=200, blank=True)
    twitter_link   =   models.URLField(max_length=200, blank=True)
    instagram_link   =   models.URLField(max_length=200, blank=True)
    linkedin_link   =   models.URLField(max_length=200, blank=True)
    profile_img =   ProcessedImageField(upload_to='images/about_images/team_members/%Y/%m/%d/', processors=[ResizeToFill(400, 400)],format='JPEG', options={'quality': 90}, blank=False)

    def __str__(self):
        return self.name


class banner(models.Model):
    main_banner =   ProcessedImageField(upload_to='site/banners/main_banner/%Y/%m/%d/', processors=[ResizeToFill(1920, 900)],format='PNG', options={'quality': 100}, blank=True)
    app_banner  =   ProcessedImageField(upload_to='site/banners/app_banner/%Y/%m/%d/', processors=[ResizeToFill(600, 600)],format='PNG', options={'quality': 100}, blank=True)
    our_story   =   ProcessedImageField(upload_to='site/banners/our_story/%Y/%m/%d/', processors=[ResizeToFill(700, 850)],format='PNG', options={'quality': 100}, blank=True)
    our_mission =   ProcessedImageField(upload_to='site/banners/our_mission/%Y/%m/%d/', processors=[ResizeToFill(700, 850)],format='PNG', options={'quality': 100}, blank=True)
    alt_text    =   models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.alt_text


    def image_tag(self):
        return mark_safe('<img src="%s" width="300" />' %(self.main_banner.url))
