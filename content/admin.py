from django.contrib import admin
from .models import banner, aboutus, membership_page, homepage, service, TeamMember
from django.utils.html import format_html

# Register your models here.

class bannerAdmin(admin.ModelAdmin):
    list_display    =   ('alt_text','image_tag',)

class aboutusAdmin(admin.ModelAdmin):
    list_display    =   ('id','our_story', 'our_mission', 'security', 'manage', 'promise', )
    list_display_links    =   ('id','our_story', 'our_mission', 'security', 'manage', 'promise', )

class TeamMemberAdmin(admin.ModelAdmin):
    def thumbmail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50;">'.format(object.profile_img.url))
    list_display    =   ('id','name', 'designation', 'thumbmail')
    list_display_links    =   ('id','name',)

admin.site.register(banner, bannerAdmin)
admin.site.register(aboutus, aboutusAdmin)
admin.site.register(membership_page)
admin.site.register(homepage)
admin.site.register(service)
admin.site.register(TeamMember, TeamMemberAdmin)
